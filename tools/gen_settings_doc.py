"""Generates SETTINGS.md from the pack's settings.glsl: every switch option and
value option, its default and (for sliders) its range, grouped by the file's own
section comments."""
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
text = (root / "shaders" / "settings.glsl").read_text(encoding="utf-8").split("\n")
out_path = root / "SETTINGS.md"

value_re = re.compile(
    r"^\s*#\s*define\s+([A-Za-z_]\w*)\s+(\S+)\s*//\s*(.*?)\s*\[([^\]]+)\]"
)
switch_on = re.compile(r"^\s*#\s*define\s+([A-Za-z_]\w*)\s*(?://.*)?$")
switch_off = re.compile(r"^\s*//\s*#\s*define\s+([A-Za-z_]\w*)\s*(?://.*)?$")

SKIP = {"SETTINGS_INCLUDED"}

section = "General"
items = []  # (section, name, kind, default, values)
for line in text:
    s = line.strip()
    m = re.match(r"^//\s{2,}([A-Za-z][A-Za-z /&()-]+?)\s*$", s)
    if m:
        name = m.group(1).strip()
        if name.lower() != "boolean options":
            section = name
        continue
    m = value_re.match(line)
    if m and m.group(1) not in SKIP:
        items.append((section, m.group(1), "value", m.group(2), m.group(4).split()))
        continue
    m = switch_off.match(line)
    if m and m.group(1) not in SKIP:
        items.append((section, m.group(1), "switch", "off", []))
        continue
    m = switch_on.match(line)
    if m and m.group(1) not in SKIP:
        items.append((section, m.group(1), "switch", "on", []))

lines = [
    "# Settings reference",
    "",
    "Every option in `shaders/settings.glsl`, as Horizon shows it in **Shader",
    "Options...**. Switch options are on/off toggles; value options are sliders (or",
    "cycle buttons) with the values listed. The Low/Medium/High/Ultra profiles set",
    "groups of them at once (`shaders.properties`, `profile.*`).",
]
current = None
for sec, name, kind, default, values in items:
    if sec != current:
        current = sec
        lines.append("")
        lines.append(f"## {sec}")
        lines.append("")
        lines.append("| Option | Default | Values |")
        lines.append("|---|---|---|")
    if kind == "switch":
        lines.append(f"| `{name}` | {'On' if default == 'on' else 'Off'} | on/off |")
    else:
        v = values
        shown = " ".join(v[:6]) + (f" ... {v[-1]} ({len(v)} values)" if len(v) > 8 else "")
        lines.append(f"| `{name}` | {default} | {shown} |")

out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"options: {len(items)} written to {out_path}")
