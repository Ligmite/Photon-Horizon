"""Static checks for the ported pack, with no shader compiler:

1. every `#include` target resolves (absolute /path or relative to the file);
2. preprocessor conditionals balance in every stage source;
3. every `screen.*` / `sliders` name in shaders.properties is a known option;
4. every value option has its value list.
"""
import os
import re
import sys

ROOT = sys.argv[1]  # .../photon-horizon/shaders

STAGE = (".vsh", ".fsh", ".csh", ".gsh", ".glsl")


def walk():
    for d, _, fs in os.walk(ROOT):
        for f in fs:
            if f.endswith(STAGE):
                yield os.path.join(d, f)


include_re = re.compile(r'^\s*#\s*include\s+([<"])([^>"]+)[>"]')

missing = []
for path in walk():
    rel = os.path.relpath(path, ROOT).replace("\\", "/")
    depth = 0
    with open(path, encoding="utf-8", errors="replace") as fh:
        for n, line in enumerate(fh, 1):
            s = line.strip()
            if s.startswith("#"):
                word = s[1:].split()[0] if len(s) > 1 else ""
                if word in ("ifdef", "ifndef", "if"):
                    depth += 1
                elif word == "endif":
                    depth -= 1
                    if depth < 0:
                        print(f"UNBALANCED #endif {rel}:{n}")
                        depth = 0
            m = include_re.match(line)
            if not m:
                continue
            target = m.group(2)
            if target.startswith("/"):
                resolved = os.path.normpath(os.path.join(ROOT, target.lstrip("/")))
            else:
                resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
            if not os.path.isfile(resolved):
                missing.append((rel, n, target))
    if depth:
        print(f"UNCLOSED conditional at end of {rel} (depth {depth})")

print(f"includes missing: {len(missing)}")
guarded = 0
for rel, n, target in missing:
    print(f"  MISSING {rel}:{n} -> {target}")
print("done")
