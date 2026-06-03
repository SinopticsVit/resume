# -*- coding: utf-8 -*-
"""Собирает единый HTML из office_setup markdown-документов.

Результат: office_setup/office_setup_concept.html
"""

import os
import re
import html
import datetime

import markdown

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OFFICE_DIR = os.path.join(BASE_DIR, "office_setup")
OUT = os.path.join(OFFICE_DIR, "office_setup_concept.html")

FILES = [
    "01_functional_structure.md",
    "02_org_structure.md",
    "03_budget_6m.md",
    "04_setup_development_plan_6m.md",
    "05_horizontal_interactions_moscow.md",
    "06_sample_delivery_scheme_payment.md",
]


def extract_title(md_text, fallback):
    lines = md_text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            del lines[i]
            return title, "\n".join(lines)
    return fallback, md_text


def fix_tight_lists(md_text):
    lines = md_text.splitlines()
    out = []
    list_re = re.compile(r"^\s*(\d+\.|[-*+])\s+\S")
    intro_re = re.compile(r":\**\s*$")
    for i, line in enumerate(lines):
        out.append(line)
        if i + 1 < len(lines):
            cur = line.strip()
            nxt = lines[i + 1]
            if cur and not list_re.match(line) and intro_re.search(cur) and list_re.match(nxt):
                out.append("")
    return "\n".join(out)


def style_task_lists(html_body):
    html_body = re.sub(
        r"<li>\[ \]\s*",
        '<li class="task"><span class="box"></span>',
        html_body,
    )
    html_body = re.sub(
        r"<li>\[[xX]\]\s*",
        '<li class="task done"><span class="box">\u2713</span>',
        html_body,
    )
    return html_body


def render_mermaid_blocks(html_body):
    """Преобразует fenced mermaid code blocks в <div class="mermaid">."""
    pattern = re.compile(
        r'<pre><code class="language-mermaid">(.*?)</code></pre>',
        re.DOTALL,
    )

    def _repl(match):
        diagram = html.unescape(match.group(1)).strip()
        return '<div class="mermaid">%s</div>' % diagram

    return pattern.sub(_repl, html_body)


CSS = """
:root{
  --bg:#f6f7f9; --card:#ffffff; --ink:#1f2733; --muted:#5b6675;
  --brand:#1f3864; --brand-2:#2f5597; --line:#e3e7ee; --soft:#eef2f8;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;font-size:16px;line-height:1.65}
.layout{display:grid;grid-template-columns:300px 1fr;max-width:1400px;margin:0 auto}
.sidebar{position:sticky;top:0;height:100vh;overflow-y:auto;padding:24px 18px;background:var(--brand);color:#dfe7f5}
.sidebar .brandmark{font-size:18px;font-weight:700;color:#fff}
.sidebar .sub{font-size:12px;color:#9db4dc;margin:6px 0 10px}
.sidebar h2{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:#9db4dc;margin:16px 0 8px}
.toc,.toc ul{list-style:none;padding:0;margin:0}
.toc a{color:#cdd9ee;text-decoration:none;display:block;padding:5px 10px;border-radius:6px;font-size:13px}
.toc a:hover{background:rgba(255,255,255,.1);color:#fff}
.toc ul{margin-left:10px;border-left:1px solid rgba(255,255,255,.15);padding-left:6px}
.content{padding:0 0 70px}
.hero{background:linear-gradient(135deg,var(--brand) 0%,var(--brand-2) 100%);color:#fff;padding:44px 48px 36px}
.hero h1{margin:0 0 10px;font-size:30px;line-height:1.2}
.hero .tagline{color:#d9e7ff;font-size:15px;max-width:860px}
.hero .pills{margin-top:16px;display:flex;flex-wrap:wrap;gap:8px}
.hero .pill{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.22);padding:5px 12px;border-radius:999px;font-size:12px}
.main{padding:34px 48px}
.main h2{font-size:23px;color:var(--brand);margin:42px 0 14px;padding-bottom:8px;border-bottom:2px solid var(--line)}
.main h3{font-size:18px;color:var(--brand-2);margin:24px 0 10px}
.main h4{font-size:15px;margin:16px 0 8px}
.main hr{border:0;border-top:1px solid var(--line);margin:30px 0}
ul,ol{padding-left:22px}
.table-wrap{overflow-x:auto;margin:16px 0;border:1px solid var(--line);border-radius:10px}
table{border-collapse:collapse;width:100%;font-size:14px;background:var(--card)}
thead th{background:var(--brand);color:#fff;text-align:left;font-weight:600;padding:10px 12px}
tbody td{padding:9px 12px;border-top:1px solid var(--line);vertical-align:top}
tbody tr:nth-child(even){background:var(--soft)}
blockquote{margin:16px 0;padding:14px 18px;background:#fff;border-left:4px solid var(--brand-2);border-radius:0 8px 8px 0;color:var(--muted)}
pre{background:#0e1c33;color:#dfe9fb;padding:16px 18px;border-radius:10px;overflow-x:auto;font-size:13px;line-height:1.5}
code{font-family:Consolas,"Liberation Mono",Menlo,monospace}
:not(pre)>code{background:var(--soft);padding:1.5px 6px;border-radius:5px;font-size:13px}
li.task{list-style:none;margin-left:-18px;display:flex;gap:8px}
li.task .box{flex:0 0 16px;width:16px;height:16px;border:1.5px solid var(--brand-2);border-radius:4px;margin-top:4px;display:inline-flex;align-items:center;justify-content:center;font-size:11px;color:#fff}
li.task.done .box{background:var(--brand-2)}
.footer{padding:22px 48px;color:var(--muted);font-size:13px;border-top:1px solid var(--line);background:var(--card)}
@media (max-width:980px){
  .layout{grid-template-columns:1fr}
  .sidebar{position:static;height:auto}
  .hero,.main,.footer{padding-left:20px;padding-right:20px}
}
"""

TEMPLATE = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
<div class="layout">
  <aside class="sidebar">
    <div class="brandmark">Детский Мир — КНР</div>
    <div class="sub">Концепция офиса в Китае (WFOE)</div>
    <h2>Содержание</h2>
    {toc}
  </aside>
  <div class="content">
    <header class="hero">
      <h1>{title}</h1>
      <div class="tagline">{tagline}</div>
      <div class="pills">{pills}</div>
    </header>
    <main class="main">
      {body}
    </main>
    <footer class="footer">
      Сгенерировано из markdown-документов папки <code>office_setup</code> · {generated}
    </footer>
  </div>
</div>
<script type="module">
  import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
  mermaid.initialize({{
    startOnLoad: true,
    securityLevel: "loose",
    theme: "default",
  }});
</script>
</body>
</html>
"""


def build_combined_markdown():
    docs = []
    for index, name in enumerate(FILES, start=1):
        path = os.path.join(OFFICE_DIR, name)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        title, body = extract_title(text, name)
        docs.append("## %02d. %s\n\n%s" % (index, title, body.strip()))
    return "\n\n---\n\n".join(docs)


def main():
    body_md = fix_tight_lists(build_combined_markdown())
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
        extension_configs={"toc": {"toc_depth": "2-3", "permalink": False}},
    )
    body_html = md.convert(body_md)
    toc_html = md.toc

    body_html = style_task_lists(body_html)
    body_html = render_mermaid_blocks(body_html)
    body_html = body_html.replace("<table>", '<div class="table-wrap"><table>')
    body_html = body_html.replace("</table>", "</table></div>")

    pills = "".join(
        '<span class="pill">%s</span>' % html.escape(p)
        for p in [
            "WFOE модель",
            "6 документов",
            "Функции + оргструктура",
            "Бюджет + финансирование",
            "SLA и процессы",
        ]
    )

    out_html = TEMPLATE.format(
        title="Концепция офиса «Детского Мира» в КНР (office_setup)",
        css=CSS,
        toc=toc_html,
        body=body_html,
        tagline="Сводный HTML по функциональной и организационной структуре, бюджету, плану запуска, взаимодействиям с Москвой и схеме работы с образцами.",
        pills=pills,
        generated=datetime.date.today().strftime("%d.%m.%Y"),
    )

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(out_html)
    print("Saved:", OUT)
    print("Size: %.1f KB" % (len(out_html) / 1024))


if __name__ == "__main__":
    main()
