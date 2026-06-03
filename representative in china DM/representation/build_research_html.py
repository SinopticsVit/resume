# -*- coding: utf-8 -*-
"""Генератор автономного HTML-отчёта из markdown-исследования.

Берёт detsky_mir_china_research_report.md и собирает самодостаточный
(offline, без CDN) HTML с боковым оглавлением, стилизованными таблицами
и print-версией.
"""

import os
import re
import html
import datetime

import markdown

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE_DIR, "detsky_mir_china_research_report.md")
OUT = os.path.join(BASE_DIR, "detsky_mir_china_research_report.html")


def extract_title(md_text):
    """Достаёт первый H1 как заголовок и удаляет его из тела."""
    lines = md_text.splitlines()
    title = "Исследование"
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            del lines[i]
            break
    return title, "\n".join(lines)


def fix_tight_lists(md_text):
    """Вставляет пустую строку между строкой-вступлением с ':' и списком,
    чтобы нумерованные/маркированные списки рендерились как списки, а не текст."""
    lines = md_text.splitlines()
    out = []
    list_re = re.compile(r"^\s*(\d+\.|[-*+])\s+\S")
    intro_re = re.compile(r":\**\s*$")
    for i, line in enumerate(lines):
        out.append(line)
        if i + 1 < len(lines):
            cur = line.strip()
            nxt = lines[i + 1]
            if (cur and not list_re.match(line) and intro_re.search(cur)
                    and list_re.match(nxt)):
                out.append("")
    return "\n".join(out)


def style_task_lists(html_body):
    """Преобразует пункты списков вида [ ] / [x] в чекбоксы."""
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
  --brand:#1f3864; --brand-2:#2f5597; --accent:#c0392b;
  --line:#e3e7ee; --soft:#eef2f8; --code:#0f2f5b;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif;
  font-size:16px; line-height:1.65;
}
.layout{display:grid; grid-template-columns:300px 1fr; align-items:start; max-width:1400px; margin:0 auto;}
/* Sidebar TOC */
.sidebar{position:sticky; top:0; height:100vh; overflow-y:auto; padding:24px 18px; background:var(--brand); color:#dfe7f5;}
.sidebar h2{font-size:13px; letter-spacing:.08em; text-transform:uppercase; color:#9db4dc; margin:18px 0 8px;}
.sidebar .brandmark{font-size:18px; font-weight:700; color:#fff; line-height:1.3; margin-bottom:6px;}
.sidebar .sub{font-size:12px; color:#9db4dc; margin-bottom:8px;}
.toc, .toc ul{list-style:none; margin:0; padding:0;}
.toc li{margin:2px 0;}
.toc a{color:#cdd9ee; text-decoration:none; display:block; padding:5px 10px; border-radius:6px; font-size:13.5px;}
.toc a:hover{background:rgba(255,255,255,.10); color:#fff;}
.toc ul{margin-left:10px; border-left:1px solid rgba(255,255,255,.15); padding-left:6px;}
.toc ul a{font-size:12.5px; color:#a9bcdd;}
/* Content */
.content{padding:0 0 80px;}
.hero{background:linear-gradient(135deg,var(--brand) 0%,var(--brand-2) 100%); color:#fff; padding:46px 48px 38px;}
.hero h1{margin:0 0 10px; font-size:30px; line-height:1.2; letter-spacing:-.01em;}
.hero .tagline{color:#cfe; opacity:.92; font-size:15px; max-width:760px;}
.hero .pills{margin-top:18px; display:flex; flex-wrap:wrap; gap:8px;}
.hero .pill{background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.22); padding:5px 12px; border-radius:999px; font-size:12.5px;}
.main{padding:34px 48px;}
.main h2{font-size:23px; color:var(--brand); margin:42px 0 14px; padding-bottom:8px; border-bottom:2px solid var(--line); scroll-margin-top:14px;}
.main h2:first-child{margin-top:6px;}
.main h3{font-size:18px; color:var(--brand-2); margin:26px 0 10px; scroll-margin-top:14px;}
.main h4{font-size:15.5px; color:var(--ink); margin:18px 0 8px; text-transform:none;}
.main p{margin:10px 0;}
.main a{color:var(--brand-2);}
.main hr{border:0; border-top:1px solid var(--line); margin:30px 0;}
ul,ol{padding-left:22px;}
li{margin:4px 0;}
strong{color:#15203a;}
/* Tables */
.table-wrap{overflow-x:auto; margin:16px 0; border:1px solid var(--line); border-radius:10px;}
table{border-collapse:collapse; width:100%; font-size:14px; background:var(--card);}
thead th{background:var(--brand); color:#fff; text-align:left; font-weight:600; padding:10px 12px; position:sticky; top:0;}
tbody td{padding:9px 12px; border-top:1px solid var(--line); vertical-align:top;}
tbody tr:nth-child(even){background:var(--soft);}
tbody tr:hover{background:#e7eefb;}
/* Blockquote callout */
blockquote{margin:16px 0; padding:14px 18px; background:#fff; border-left:4px solid var(--brand-2);
  border-radius:0 8px 8px 0; color:var(--muted); box-shadow:0 1px 2px rgba(20,40,80,.05);}
blockquote p{margin:6px 0;}
/* Code */
pre{background:#0e1c33; color:#dfe9fb; padding:16px 18px; border-radius:10px; overflow-x:auto; font-size:13px; line-height:1.5;}
code{font-family:"SFMono-Regular",Consolas,"Liberation Mono",Menlo,monospace;}
:not(pre)>code{background:var(--soft); color:var(--code); padding:1.5px 6px; border-radius:5px; font-size:13.5px;}
/* Task lists */
li.task{list-style:none; margin-left:-18px; display:flex; align-items:flex-start; gap:8px;}
li.task .box{flex:0 0 16px; width:16px; height:16px; border:1.5px solid var(--brand-2); border-radius:4px; margin-top:4px;
  display:inline-flex; align-items:center; justify-content:center; font-size:11px; color:#fff;}
li.task.done .box{background:var(--brand-2);}
/* Footer */
.footer{padding:22px 48px; color:var(--muted); font-size:13px; border-top:1px solid var(--line); background:var(--card);}
.toc-toggle{display:none;}
@media (max-width:980px){
  .layout{grid-template-columns:1fr;}
  .sidebar{position:static; height:auto; max-height:none;}
  .hero,.main,.footer{padding-left:20px; padding-right:20px;}
}
@media print{
  body{background:#fff; font-size:11.5px;}
  .layout{display:block; max-width:none;}
  .sidebar{display:none;}
  .hero{background:#1f3864 !important; -webkit-print-color-adjust:exact; print-color-adjust:exact;}
  thead th{background:#1f3864 !important; -webkit-print-color-adjust:exact; print-color-adjust:exact;}
  .main h2{page-break-after:avoid;} table,pre,blockquote{page-break-inside:avoid;}
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
    <div class="sub">Исследование открытия офиса</div>
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
      Сгенерировано из <code>detsky_mir_china_research_report.md</code> · {generated}
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


def main():
    with open(SRC, encoding="utf-8") as fh:
        md_text = fh.read()

    title, body_md = extract_title(md_text)
    body_md = fix_tight_lists(body_md)

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
        extension_configs={"toc": {"toc_depth": "2-3", "permalink": False}},
    )
    body_html = md.convert(body_md)
    toc_html = md.toc  # сгенерированное оглавление

    # Тюнинг тела
    body_html = style_task_lists(body_html)
    body_html = render_mermaid_blocks(body_html)
    # Оборачиваем таблицы в скролл-контейнеры
    body_html = body_html.replace("<table>", '<div class="table-wrap"><table>')
    body_html = body_html.replace("</table>", "</table></div>")

    # Тэглайн / pills из метаданных
    tagline = ("Desk research по открытию присутствия «Детского Мира» в КНР: "
               "рынок, конкуренты, право, логистика, финансовая модель, риски и дорожная карта.")
    pills = "".join(
        '<span class="pill">%s</span>' % html.escape(p)
        for p in ["Горизонт 2022–2030", "10 блоков", "Desk research",
                  "Sourcing + QC", "Финансовая модель"]
    )

    out_html = TEMPLATE.format(
        title=html.escape(title),
        css=CSS,
        toc=toc_html,
        body=body_html,
        tagline=tagline,
        pills=pills,
        generated=datetime.date.today().strftime("%d.%m.%Y"),
    )

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(out_html)
    print("Saved:", OUT)
    print("Size: %.1f KB" % (len(out_html) / 1024))


if __name__ == "__main__":
    main()
