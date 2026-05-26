# -*- coding: utf-8 -*-
"""Convert Markdown resumes to standalone HTML."""
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MD_PATH = os.path.join(ROOT, "Senior_Business_Analyst_RU.md")
DEFAULT_HTML_PATH = os.path.join(ROOT, "Senior_Business_Analyst_RU.html")


def infer_html_lang(md_path: str) -> str:
    filename = os.path.splitext(os.path.basename(md_path))[0].upper()
    if filename.endswith("_EN"):
        return "en"
    if filename.endswith("_RU"):
        return "ru"
    return "ru"


def apply_inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*\n]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text.replace("  ", "<br />")


def parse_table(lines):
    rows = []
    for ln in lines:
        ln = ln.strip()
        if re.match(r"^\|[-| :]+\|$", ln):
            continue
        if ln.startswith("|"):
            rows.append([apply_inline(c.strip()) for c in ln.strip("|").split("|")])
    return rows


def render_table(rows):
    if not rows:
        return ""
    head = rows[0]
    body = rows[1:]
    out = [
        "<table>",
        "  <thead>",
        "    <tr>",
        *(f"      <th scope=\"col\">{cell}</th>" for cell in head),
        "    </tr>",
        "  </thead>",
        "  <tbody>",
    ]
    for row in body:
        out.append("    <tr>")
        for i, cell in enumerate(row):
            tag = "th" if i == 0 else "td"
            scope = ' scope="row"' if i == 0 else ""
            out.append(f"      <{tag}{scope}>{cell}</{tag}>")
        out.append("    </tr>")
    out.extend(["  </tbody>", "</table>"])
    return "\n".join(out)


def parse_markdown(md_text: str):
    lines = md_text.splitlines()
    i = 0
    blocks = []
    while i < len(lines):
        stripped = lines[i].strip()

        if not stripped:
            i += 1
            continue

        if re.match(r"^-{3,}$|^\*{3,}$", stripped):
            blocks.append({"type": "hr"})
            i += 1
            continue

        if stripped.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            blocks.append({"type": "table", "rows": parse_table(table_lines)})
            continue

        m = re.match(r"^# (.+)$", stripped)
        if m:
            blocks.append({"type": "h1", "text": apply_inline(m.group(1))})
            i += 1
            continue

        m = re.match(r"^## (.+)$", stripped)
        if m:
            blocks.append({"type": "h2", "text": apply_inline(m.group(1))})
            i += 1
            continue

        m = re.match(r"^### (.+)$", stripped)
        if m:
            blocks.append({"type": "h3", "text": apply_inline(m.group(1))})
            i += 1
            continue

        m = re.match(r"^\*([^*].+?)\*\s*(.*)$", stripped)
        if m:
            text = m.group(1) + (" " + m.group(2) if m.group(2) else "")
            blocks.append({"type": "meta", "text": apply_inline(text)})
            i += 1
            continue

        m = re.match(r"^[-*] (.+)$", stripped)
        if m:
            items = []
            while i < len(lines):
                mm = re.match(r"^[-*] (.+)$", lines[i].strip())
                if not mm:
                    break
                items.append(apply_inline(mm.group(1)))
                i += 1
            blocks.append({"type": "ul", "items": items})
            continue

        paragraph = [apply_inline(stripped)]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or re.match(r"^(#|##|###) ", nxt) or re.match(r"^-{3,}$|^\*{3,}$", nxt):
                break
            if nxt.startswith("|") or re.match(r"^[-*] ", nxt) or re.match(r"^\*([^*].+?)\*\s*(.*)$", nxt):
                break
            paragraph.append(apply_inline(nxt))
            i += 1
        blocks.append({"type": "p", "text": " ".join(paragraph)})
    return blocks


def render_html(md_text: str, title: str, lang: str) -> str:
    blocks = parse_markdown(md_text)
    body = []
    for block in blocks:
        t = block["type"]
        if t == "h1":
            body.append(f"<h1>{block['text']}</h1>")
        elif t == "h2":
            body.append(f"<h2>{block['text']}</h2>")
        elif t == "h3":
            body.append(f"<h3>{block['text']}</h3>")
        elif t == "meta":
            body.append(f"<p class=\"meta-line\"><em>{block['text']}</em></p>")
        elif t == "p":
            body.append(f"<p>{block['text']}</p>")
        elif t == "ul":
            items = "\n".join(f"  <li>{item}</li>" for item in block["items"])
            body.append(f"<ul>\n{items}\n</ul>")
        elif t == "table":
            body.append(render_table(block["rows"]))
        elif t == "hr":
            body.append("<hr />")

    return f"""<!DOCTYPE html>
<html lang="{html.escape(lang)}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)}</title>
  <style>
    :root {{
      --text: #1a1a1a;
      --muted: #555;
      --border: #d0d7de;
      --accent: #0d47a1;
      --bg-soft: #f6f8fa;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0 auto;
      max-width: 210mm;
      padding: 14mm 16mm 18mm;
      font-family: "Segoe UI", system-ui, -apple-system, Roboto, Arial, sans-serif;
      font-size: 10.5pt;
      line-height: 1.45;
      color: var(--text);
      background: #fff;
    }}
    h1 {{
      margin: 0 0 0.35rem;
      font-size: 1.7rem;
      font-weight: 700;
      letter-spacing: -0.02em;
    }}
    h2 {{
      margin: 1.2rem 0 0.45rem;
      padding-bottom: 0.2rem;
      font-size: 0.88rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--accent);
      border-bottom: 1px solid var(--border);
    }}
    h3 {{
      margin: 0.9rem 0 0.2rem;
      font-size: 1rem;
    }}
    p {{
      margin: 0.35rem 0;
    }}
    .meta-line {{
      margin-top: 0;
      color: var(--muted);
      font-size: 0.93rem;
    }}
    ul {{
      margin: 0.25rem 0 0.55rem;
      padding-left: 1.15rem;
    }}
    li {{
      margin: 0.18rem 0;
    }}
    hr {{
      border: 0;
      border-top: 1px solid var(--border);
      margin: 0.8rem 0;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 0.4rem 0 0.7rem;
      font-size: 9.7pt;
    }}
    th, td {{
      border: 1px solid var(--border);
      padding: 0.35rem 0.5rem;
      vertical-align: top;
      text-align: left;
    }}
    thead th {{
      background: var(--bg-soft);
    }}
    tbody th {{
      width: 28%;
      font-weight: 600;
      background: #fcfcfc;
    }}
    code {{
      font-family: Consolas, "Courier New", monospace;
      font-size: 0.94em;
    }}
    a {{
      color: inherit;
    }}
    @page {{
      size: A4;
      margin: 12mm 14mm 14mm;
    }}
    @media print {{
      body {{
        padding: 0;
        max-width: none;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }}
      h2, h3 {{
        break-after: avoid;
      }}
      ul, table {{
        break-inside: avoid;
      }}
    }}
  </style>
</head>
<body>
{os.linesep.join(body)}
</body>
</html>
"""


def main():
    md_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MD_PATH
    html_path = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_HTML_PATH

    with open(md_path, "r", encoding="utf-8") as fh:
        md_text = fh.read()

    title = os.path.splitext(os.path.basename(md_path))[0]
    rendered = render_html(md_text, title, infer_html_lang(md_path))

    with open(html_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(rendered)

    print("OK ->", html_path)


if __name__ == "__main__":
    main()
