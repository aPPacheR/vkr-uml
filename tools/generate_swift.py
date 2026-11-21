import re
import sys
from pathlib import Path

src = Path(sys.argv[1]).read_text(encoding="utf-8")
out = Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)

TYPES = {"int": "Int", "string": "String", "boolean": "Bool", "bool": "Bool",
         "date": "Date", "double": "Double", "float": "Float", "long": "Int64"}

def conv(t):
    t = t.strip()
    m = re.match(r"List<(.+)>$", t)
    if m:
        return f"[{conv(m.group(1))}]"
    m = re.match(r"Set<(.+)>$", t)
    if m:
        return f"Set<{conv(m.group(1))}>"
    return TYPES.get(t.lower(), t)

for m in re.finditer(r"class\s+(\w+)\s*\{(.*?)\}", src, re.S):
    name, body = m.group(1), m.group(2)
    fields, methods = [], []
    for line in body.splitlines():
        line = line.strip()
        if not line or line[0] not in "+-#":
            continue
        vis = "private " if line[0] == "-" else ""
        line = line[1:].strip()
        if "(" in line:
            mm = re.match(r"(\w+)\((.*?)\)\s*:?\s*(.*)", line)
            mname, args, ret = mm.group(1), mm.group(2), mm.group(3)
            params = []
            for a in filter(None, [x.strip() for x in args.split(",")]):
                n, _, t = a.partition(":")
                params.append(f"{n.strip()}: {conv(t)}")
            ret = f" -> {conv(ret)}" if ret.strip() else ""
            methods.append(f"    {vis}func {mname}({', '.join(params)}){ret} {{\n        fatalError(\"not implemented\")\n    }}")
        else:
            n, _, t = line.partition(":")
            fields.append((vis, n.strip(), conv(t)))
    lines = ["import Foundation", "", f"final class {name} {{"]
    for vis, n, t in fields:
        lines.append(f"    {vis}let {n}: {t}")
    if fields:
        lines.append("")
        params = ", ".join(f"{n}: {t}" for _, n, t in fields)
        lines.append(f"    init({params}) {{")
        for _, n, _t in fields:
            lines.append(f"        self.{n} = {n}")
        lines.append("    }")
    if methods:
        lines.append("")
        lines.append("\n\n".join(methods))
    lines.append("}")
    (out / f"{name}.swift").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("создан", out / f"{name}.swift")