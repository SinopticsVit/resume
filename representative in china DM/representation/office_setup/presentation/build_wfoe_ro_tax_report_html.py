# -*- coding: utf-8 -*-
"""Собирает HTML из wfoe-vs-ro-tax-report.md.

Результат: presentation/wfoe-vs-ro-tax-report.html
"""

import datetime
import html
import os
import re

import markdown

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE_DIR, "wfoe-vs-ro-tax-report.md")
OUT = os.path.join(BASE_DIR, "wfoe-vs-ro-tax-report.html")

CSS = """
:root{
  --bg:#f6f7f9; --card:#ffffff; --ink:#1f2733; --muted:#5b6675;
  --brand:#1f3864; --brand-2:#2f5597; --accent:#0d7377; --line:#e3e7ee; --soft:#eef2f8;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;font-size:16px;line-height:1.65}
.layout{display:grid;grid-template-columns:300px 1fr;max-width:1400px;margin:0 auto}
.sidebar{position:sticky;top:0;height:100vh;overflow-y:auto;padding:24px 18px;background:var(--brand);color:#dfe7f5}
.sidebar .brandmark{font-size:18px;font-weight:700;color:#fff;line-height:1.3}
.sidebar .sub{font-size:12px;color:#9db4dc;margin:6px 0 10px}
.sidebar h2{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:#9db4dc;margin:16px 0 8px}
.toc,.toc ul{list-style:none;padding:0;margin:0}
.toc a{color:#cdd9ee;text-decoration:none;display:block;padding:5px 10px;border-radius:6px;font-size:13px}
.toc a:hover{background:rgba(255,255,255,.1);color:#fff}
.toc ul{margin-left:10px;border-left:1px solid rgba(255,255,255,.15);padding-left:6px}
.toc ul a{font-size:12px;color:#a9bcdd}
.content{padding:0 0 70px}
.hero{background:linear-gradient(135deg,var(--brand) 0%,var(--accent) 100%);color:#fff;padding:44px 48px 36px}
.hero h1{margin:0 0 10px;font-size:28px;line-height:1.25}
.hero .tagline{color:#d9e7ff;font-size:15px;max-width:860px}
.hero .pills{margin-top:16px;display:flex;flex-wrap:wrap;gap:8px}
.hero .pill{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.22);padding:5px 12px;border-radius:999px;font-size:12px}
.main{padding:34px 48px}
.main h2{font-size:23px;color:var(--brand);margin:42px 0 14px;padding-bottom:8px;border-bottom:2px solid var(--line);scroll-margin-top:14px}
.main h2:first-child{margin-top:6px}
.main h3{font-size:18px;color:var(--brand-2);margin:24px 0 10px;scroll-margin-top:14px}
.main h4{font-size:15px;margin:16px 0 8px}
.main p{margin:10px 0}
.main a{color:var(--brand-2)}
.main hr{border:0;border-top:1px solid var(--line);margin:30px 0}
ul,ol{padding-left:22px}
li{margin:4px 0}
strong{color:#15203a}
.table-wrap{overflow-x:auto;margin:16px 0;border:1px solid var(--line);border-radius:10px}
table{border-collapse:collapse;width:100%;font-size:14px;background:var(--card)}
thead th{background:var(--brand);color:#fff;text-align:left;font-weight:600;padding:10px 12px}
tbody td{padding:9px 12px;border-top:1px solid var(--line);vertical-align:top}
tbody tr:nth-child(even){background:var(--soft)}
tbody tr:hover{background:#e7eefb}
blockquote{margin:16px 0;padding:14px 18px;background:#fff;border-left:4px solid var(--accent);border-radius:0 8px 8px 0;color:var(--muted);box-shadow:0 1px 2px rgba(20,40,80,.05)}
blockquote p{margin:6px 0}
pre{background:#0e1c33;color:#dfe9fb;padding:16px 18px;border-radius:10px;overflow-x:auto;font-size:13px;line-height:1.5}
code{font-family:Consolas,"Liberation Mono",Menlo,monospace}
:not(pre)>code{background:var(--soft);padding:1.5px 6px;border-radius:5px;font-size:13px}
.mermaid{margin:20px 0;padding:16px;background:var(--card);border:1px solid var(--line);border-radius:10px;text-align:center}
.footer{padding:22px 48px;color:var(--muted);font-size:13px;border-top:1px solid var(--line);background:var(--card)}
@media (max-width:980px){
  .layout{grid-template-columns:1fr}
  .sidebar{position:static;height:auto}
  .hero,.main,.footer{padding-left:20px;padding-right:20px}
}
@media print{
  body{background:#fff;font-size:11.5px}
  .layout{display:block;max-width:none}
  .sidebar{display:none}
  .hero{background:var(--brand)!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  thead th{background:var(--brand)!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  .main h2{page-break-after:avoid}
  table,pre,blockquote,.mermaid{page-break-inside:avoid}
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
    <div class="sub">WFOE vs RO · налоги Фазы 1</div>
    <h2>Содержание</h2>
    {toc}
  </aside>
  <div class="content">
    <header class="hero">
      <h1>{hero_title}</h1>
      <div class="tagline">{tagline}</div>
      <div class="pills">{pills}</div>
    </header>
    <main class="main">
      {body}
    </main>
    <footer class="footer">
      Сгенерировано из <code>wfoe-vs-ro-tax-report.md</code> · {generated}
      · <a href="wfoe-vs-ro-tax-report.md">Markdown</a>
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


def render_mermaid_blocks(html_body):
    pattern = re.compile(
        r'<pre><code class="language-mermaid">(.*?)</code></pre>',
        re.DOTALL,
    )

    def _repl(match):
        diagram = html.unescape(match.group(1)).strip()
        return '<div class="mermaid">%s</div>' % diagram

    return pattern.sub(_repl, html_body)


def extract_lead(md_text):
    """Убирает H1 и blockquote-метаданные из тела (они идут в hero)."""
    lines = md_text.splitlines()
    hero_title = "WFOE vs RO: налоги и модель Фазы 1"
    body_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            hero_title = line[2:].strip()
            i += 1
            continue
        if line.startswith("> ") and not body_lines:
            while i < len(lines) and (lines[i].startswith(">") or lines[i].strip() == ""):
                i += 1
            if i < len(lines) and lines[i].strip() == "---":
                i += 1
            continue
        body_lines.append(line)
        i += 1
    return hero_title, "\n".join(body_lines).lstrip()


def main():
    with open(SRC, encoding="utf-8") as fh:
        md_text = fh.read()

    hero_title, body_md = extract_lead(md_text)

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
        extension_configs={"toc": {"toc_depth": "2-4", "permalink": False}},
    )
    body_html = md.convert(body_md)
    toc_html = md.toc

    body_html = render_mermaid_blocks(body_html)
    body_html = body_html.replace("<table>", '<div class="table-wrap"><table>')
    body_html = body_html.replace("</table>", "</table></div>")

    pills = "".join(
        '<span class="pill">%s</span>' % html.escape(p)
        for p in [
            "WFOE cost-plus 8%",
            "RO deemed profit",
            "6 мес. · 1,73 млн CNY",
            "Zero-rating НДС",
            "Фаза 1 без торговли",
        ]
    )

    out_html = TEMPLATE.format(
        title=html.escape(hero_title),
        css=CSS,
        toc=toc_html,
        hero_title=html.escape(hero_title),
        body=body_html,
        tagline=(
            "Аналитический отчёт: сравнение налогообложения RO и WFOE "
            "по китайскому законодательству и цифрам модели «Детского Мира»."
        ),
        pills=pills,
        generated=datetime.date.today().strftime("%d.%m.%Y"),
    )

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(out_html)
    print("Saved:", OUT)
    print("Size: %.1f KB" % (len(out_html) / 1024))


if __name__ == "__main__":
    main()
