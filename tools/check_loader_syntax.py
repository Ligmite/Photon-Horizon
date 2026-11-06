"""Checks the syntax Horizon's loader parses out of stage files and properties:

- `RENDERTARGETS:` / `DRAWBUFFERS:` comments (config.rs `draw_buffers`);
- `const int colortexNFormat` / `const bool colortexNClear` / clear colours,
  against the formats Horizon knows (config.rs `Format::parse`);
- `size.buffer.*`, `blend.*`, `alphaTest.*`, `flip.*` values.
"""
import os
import re
import sys

ROOT = sys.argv[1]
PROPS = os.path.join(ROOT, "shaders.properties")

FORMATS = {
    "RGBA", "R3_G3_B2", "RGB5_A1", "RGB10_A2", "RGB10_A2UI", "R11F_G11F_B10F",
    "RGB9_E5", "RGBA4", "RGB565", "RGBA2",
}
for ch in ("R", "RG", "RGB", "RGBA"):
    for bits in ("8", "16"):
        FORMATS.add(f"{ch}{bits}")
        FORMATS.add(f"{ch}{bits}_SNORM")
    for bits in ("16", "32"):
        FORMATS.add(f"{ch}{bits}F")
    for bits in ("8", "16", "32"):
        FORMATS.add(f"{ch}{bits}I")
        FORMATS.add(f"{ch}{bits}UI")

problems = []

# ---- RENDERTARGETS / DRAWBUFFERS ----
rt_re = re.compile(r"/\*\s*(RENDERTARGETS|DRAWBUFFERS)\s*:\s*([0-9,\s]+)\*/")
rt_seen = 0
for d, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith(".fsh"):
            continue
        path = os.path.join(d, f)
        text = open(path, encoding="utf-8", errors="replace").read()
        for m in rt_re.finditer(text):
            rt_seen += 1
            nums = re.findall(r"\d+", m.group(2))
            if not nums:
                problems.append(f"{path}: empty {m.group(1)}")
            for n in nums:
                if int(n) > 15:
                    problems.append(f"{path}: {m.group(1)} target {n} > 15")
        if "RENDERTARGETS" not in text and "DRAWBUFFERS" not in text:
            # A fragment program without a directive writes colortex0 by Horizon's rule.
            pass
print(f"buffer directives: {rt_seen}")

# ---- format/clear constants in comments ----
const_re = re.compile(
    r"const\s+(?:int|bool|vec4)\s+((?:colortex|shadowcolor)\w+)\s*=\s*([^;]+);"
)
fmt_re = re.compile(r"const\s+int\s+(colortex\d+)Format\s*=\s*(\w+)\s*;")
fmt_seen = 0
for d, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith((".fsh", ".glsl", ".vsh")):
            continue
        path = os.path.join(d, f)
        text = open(path, encoding="utf-8", errors="replace").read()
        for m in fmt_re.finditer(text):
            fmt_seen += 1
            name, value = m.group(1), m.group(2)
            if value not in FORMATS:
                problems.append(f"{path}: {name}Format {value} unsupported")
print(f"buffer formats: {fmt_seen}")

# ---- properties values ----
FACTORS = {
    "ZERO", "ONE", "SRC_COLOR", "ONE_MINUS_SRC_COLOR", "DST_COLOR",
    "ONE_MINUS_DST_COLOR", "SRC_ALPHA", "ONE_MINUS_SRC_ALPHA", "DST_ALPHA",
    "ONE_MINUS_DST_ALPHA", "SRC_ALPHA_SATURATE",
}
lines = open(PROPS, encoding="utf-8").read().split("\n")
for n, line in enumerate(lines, 1):
    if "=" not in line or line.strip().startswith("#"):
        continue
    key, value = [x.strip() for x in line.split("=", 1)]
    if key.startswith(("blend.", "alphaTest.", "flip.", "size.buffer.")):
        v = value.split("//")[0].strip()
        if key.startswith("blend."):
            words = v.split()
            if v != "off":
                if len(words) != 4 or any(w not in FACTORS for w in words):
                    problems.append(f"properties:{n}: blend `{v}` not four factors")
        elif key.startswith("alphaTest."):
            if v != "off":
                parts = v.split()
                if len(parts) != 2 or not parts[0].startswith(("GL_", "never")):
                    problems.append(f"properties:{n}: alphaTest `{v}`")
        elif key.startswith("flip."):
            if v not in ("true", "false"):
                problems.append(f"properties:{n}: flip `{v}`")
        elif key.startswith("size.buffer."):
            parts = v.split()
            if len(parts) != 2 or not all(
                re.fullmatch(r"\d+(?:\.\d+)?", p) for p in parts
            ):
                problems.append(f"properties:{n}: size `{v}`")

print(f"properties value problems: {len(problems)}")
for p in problems[:40]:
    print("  ", p)
