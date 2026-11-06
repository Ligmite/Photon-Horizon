"""Cross-checks the pack's options against its screens and sliders.

Options: `#define NAME` switches and `#define NAME VALUE // [..]` value options
anywhere under shaders/ (Horizon reads every stage/include file). Screens:
`screen*` names in shaders.properties. Reports screen/slider names that are not
options (they would be dropped silently) and value options without a value list.
"""
import os
import re
import sys

ROOT = sys.argv[1]
STAGE = (".vsh", ".fsh", ".csh", ".glsl")

switch_re = re.compile(r"^(?:\s*//)?\s*#\s*define\s+([A-Za-z_][A-Za-z0-9_]*)\s*(?://.*)?$")
value_re = re.compile(
    r"^\s*#\s*define\s+([A-Za-z_][A-Za-z0-9_]*)\s+(\S+)\s*//.*\[([^\]]+)\]"
)
const_re = re.compile(r"^\s*const\s+\w+\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*[^;]+;\s*//.*\[([^\]]+)\]")

switches, values, consts = set(), {}, {}
for d, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith(STAGE):
            continue
        path = os.path.join(d, f)
        for line in open(path, encoding="utf-8", errors="replace"):
            m = value_re.match(line)
            if m:
                values[m.group(1)] = m.group(3).split()
                continue
            m = switch_re.match(line)
            if m:
                switches.add(m.group(1))
                continue
            m = const_re.match(line)
            if m:
                consts[m.group(1)] = m.group(2).split()

options = set(switches) | set(values) | set(consts)
print(f"options: {len(switches)} switches, {len(values)} value options, {len(consts)} consts")

props = open(os.path.join(ROOT, "shaders.properties"), encoding="utf-8").read().split("\n")
screen_tokens = set()
sliders = []
for line in props:
    key = line.split("=", 1)[0].strip()
    if key.startswith("screen"):
        for tok in line.split("=", 1)[1].split():
            if tok.startswith("[") or tok in ("<empty>", "<profile>", "*"):
                continue
            screen_tokens.add(tok)
    elif key == "sliders":
        sliders = line.split("=", 1)[1].split()
    elif key.startswith("profile."):
        for tok in line.split("=", 1)[1].split():
            tok = tok.lstrip("!")
            if tok and "=" not in tok:
                screen_tokens.add(tok)

unknown = sorted(t for t in screen_tokens if t not in options)
print(f"screen/profile names not options ({len(unknown)}):")
for t in unknown:
    print("  ", t)

bad_sliders = sorted(t for t in sliders if t not in options)
print(f"sliders not options ({len(bad_sliders)}):")
for t in bad_sliders:
    print("  ", t)

no_list = [n for n in values if not values[n]]
print(f"value options without a list: {no_list}")
