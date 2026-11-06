"""Approximates Horizon's preprocessing of every program stub to find includes
that would be reached and are missing.

It evaluates `#if/#ifdef/#ifndef/#elif/#else/#endif` with the macro set Horizon
gives a pack (the standard macros, the renderer's, the pack's options), expands
object-like macros in expressions, and walks includes recursively. It is not a
GLSL compiler: it only proves that no *reached* `#include` points at a file the
pack does not have.
"""
import os
import re
import sys

ROOT = sys.argv[1]
FOLDERS = ["", "world0", "world-1", "world1"]

# ---------------- macros Horizon defines before reading a pack -----------------
FIXED = {
    "MC_VERSION": "260300",
    "MC_GL_VERSION": "330",
    "MC_GLSL_VERSION": "330",
    "IS_IRIS": "1",
    "IRIS_VERSION": "11107",
    "MC_RENDER_QUALITY": "1.0",
    "MC_SHADOW_QUALITY": "1.0",
    "MC_HAND_DEPTH": "0.125",
    "MAX_COLOR_BUFFERS": "16",
    "MC_NORMAL_MAP": "1",
    "MC_SPECULAR_MAP": "1",
    "MC_GL_VENDOR_OTHER": "1",
    "MC_GL_RENDERER_OTHER": "1",
    "MC_MIPMAP_LEVEL": "4",
    "IRIS_HAS_TRANSLUCENCY_SORTING": "1",
}
STAGES = [
    "NONE", "SKY", "SUNSET", "CUSTOM_SKY", "SUN", "MOON", "STARS", "VOID",
    "TERRAIN_SOLID", "TERRAIN_CUTOUT_MIPPED", "TERRAIN_CUTOUT", "ENTITIES",
    "BLOCK_ENTITIES", "DESTROY", "OUTLINE", "DEBUG", "HAND_SOLID",
    "TERRAIN_TRANSLUCENT", "TRIPWIRE", "PARTICLES", "CLOUDS", "RAIN_SNOW",
    "WORLD_BORDER", "HAND_TRANSLUCENT",
]
for i, s in enumerate(STAGES):
    FIXED[f"MC_RENDER_STAGE_{s}"] = str(i)

# Horizon's optional feature flags, as the pack asks for them.
for f in ("CUSTOM_IMAGES", "ENTITY_TRANSLUCENT"):
    FIXED[f"IRIS_FEATURE_{f}"] = "1"

# ---------------- options from settings.glsl (and other sources) ---------------
value_re = re.compile(
    r"^\s*#\s*define\s+([A-Za-z_][A-Za-z0-9_]*)\s+(\S+)\s*//.*\[[^\]]+\]"
)
switch_on = re.compile(r"^\s*#\s*define\s+([A-Za-z_][A-Za-z0-9_]*)\s*(?://.*)?$")
switch_off = re.compile(r"^\s*//\s*#\s*define\s+([A-Za-z_][A-Za-z0-9_]*)\s*(?://.*)?$")

OPTIONS = {}
TESTED = set()
for d, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith((".vsh", ".fsh", ".csh", ".glsl")):
            continue
        for line in open(os.path.join(d, f), encoding="utf-8", errors="replace"):
            m = value_re.match(line)
            if m:
                OPTIONS.setdefault(m.group(1), m.group(2))
                continue
            m = switch_off.match(line)
            if m:
                OPTIONS.setdefault(m.group(1), None)
                continue
            m = switch_on.match(line)
            if m:
                OPTIONS.setdefault(m.group(1), "1")
                continue
            if re.match(r"^\s*#\s*(ifdef|ifndef)\s+\w+", line):
                TESTED.add(line.split()[1])

BASE = dict(FIXED)
for name, val in OPTIONS.items():
    if val is not None:
        BASE[name] = val

IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def expand(expr, macros):
    prev = None
    while prev != expr:
        prev = expr
        expr = IDENT.sub(lambda m: macros.get(m.group(0), m.group(0)), expr)
    return expr


def evaluate(expr, macros):
    expr = expand(expr, macros)
    expr = re.sub(r"defined\s*\(\s*([A-Za-z_]\w*)\s*\)",
                  lambda m: "1" if m.group(1) in macros else "0", expr)
    expr = re.sub(r"defined\s+([A-Za-z_]\w*)",
                  lambda m: "1" if m.group(1) in macros else "0", expr)
    expr = IDENT.sub("0", expr)  # unknown identifiers read 0
    expr = expr.replace("&&", " and ").replace("||", " or ")
    expr = re.sub(r"!(?!=)", " not ", expr)
    try:
        return bool(eval(expr, {"__builtins__": {}}, {}))
    except Exception:
        return False


include_re = re.compile(r'^\s*#\s*include\s+([<"])([^>"]+)[>"]')


def resolve(target, cur):
    if target.startswith("/"):
        return os.path.normpath(os.path.join(ROOT, target.lstrip("/")))
    return os.path.normpath(os.path.join(os.path.dirname(cur), target))


missing = []
reached = 0


def walk(path, macros, stack=()):
    global reached
    if path in stack:
        return
    if not os.path.isfile(path):
        return
    stack = stack + (path,)
    active = True
    cond = []  # (taken_yet, active_before)
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            s = line.strip()
            if s.startswith("#"):
                word = s[1:].split()[0] if len(s) > 1 else ""
                if word in ("ifdef", "ifndef", "if"):
                    if not active:
                        cond.append((True, False))
                    else:
                        name = s.split()[1] if len(s.split()) > 1 else ""
                        if word == "ifdef":
                            ok = name in macros
                        elif word == "ifndef":
                            ok = name not in macros
                        else:
                            ok = evaluate(s[2:].strip(), macros)
                        cond.append((ok, active))
                        active = ok
                    continue
                if word == "elif":
                    if cond:
                        taken, before = cond.pop()
                        if before and not taken:
                            ok = evaluate(s[4:].strip(), macros)
                            cond.append((ok, before))
                            active = ok
                        else:
                            cond.append((taken, before))
                            active = False
                    continue
                if word == "else":
                    if cond:
                        taken, before = cond.pop()
                        active = before and not taken
                        cond.append((True, before))
                    continue
                if word == "endif":
                    if cond:
                        _, before = cond.pop()
                        active = before
                    continue
                if not active:
                    continue
                m = re.match(r"#\s*define\s+([A-Za-z_]\w*)\s+(.*)$", s)
                if m:
                    macros[m.group(1)] = m.group(2).split("//")[0].strip()
                    continue
                m = re.match(r"#\s*undef\s+([A-Za-z_]\w*)", s)
                if m:
                    macros.pop(m.group(1), None)
                    continue
                m = include_re.match(line)
                if m:
                    reached += 1
                    target = m.group(2)
                    full = resolve(target, path)
                    if not os.path.isfile(full):
                        missing.append((path, target))
                    else:
                        walk(full, macros, stack)
                    continue
    return


stubs = []
for folder in FOLDERS:
    d = os.path.join(ROOT, folder) if folder else ROOT
    if not os.path.isdir(d):
        continue
    for f in os.listdir(d):
        if f.endswith((".vsh", ".fsh", ".csh")):
            stubs.append(os.path.join(d, f))

print(f"program stubs: {len(stubs)}, options: {len(OPTIONS)}")
for stub in sorted(stubs):
    walk(stub, dict(BASE))

print(f"includes reached: {reached}")
print(f"missing reached includes: {len(missing)}")
for path, target in missing[:40]:
    print(f"  {os.path.relpath(path, ROOT)} -> {target}")
