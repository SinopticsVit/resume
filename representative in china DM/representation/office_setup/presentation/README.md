# Презентация WFOE «Детский Мир» в КНР — индекс материалов

Папка содержит **слайды и спецификацию** для сборки PowerPoint по результатам исследования в `office_setup/` (документы 01–06).

## Что внутри

| Файл | Назначение |
|---|---|
| [concept.md](./concept.md) | Концепция дека: аудитория, цели, тайминг, термины |
| [slides.md](./slides.md) | **15 слайдов** — источник истины для текста, mermaid и таблиц |
| [diagrams.md](./diagrams.md) | **Все 8 блок-схем** в одном файле (просмотр mermaid + инструкции вставки в PPTX) |
| [director-interview-questions.md](./director-interview-questions.md) | **20 вопросов** от «Детского Мира» к кандидату на директора (по презентации) |
| [wfoe-vs-ro-tax-report.md](./wfoe-vs-ro-tax-report.md) | **WFOE vs RO:** налоги, cost-plus, расчёт 6 мес. — обоснование формы (ответ на вопрос №1) |
| [wfoe-vs-ro-tax-report.html](./wfoe-vs-ro-tax-report.html) | HTML-версия отчёта (sidebar, таблицы, mermaid) |
| [build-spec.md](./build-spec.md) | Спецификация для `build_pptx.py`: diagram_id, table_id, layout, цвета, CLI |
| [_assets/diagrams/](./_assets/diagrams/) | 8 файлов `.mmd` для mermaid-cli |

## Связь с исследованием

| Слайды | Документ-источник |
|---|---|
| 2–5 | [01_functional_structure.md](../01_functional_structure.md) |
| 6–7 | [02_org_structure.md](../02_org_structure.md) |
| 8–10 | [03_budget_6m.md](../03_budget_6m.md) |
| 11–12 | [04_setup_development_plan_6m.md](../04_setup_development_plan_6m.md) |
| 13–14 | [05_horizontal_interactions_moscow.md](../05_horizontal_interactions_moscow.md), [06_sample_delivery_scheme_payment.md](../06_sample_delivery_scheme_payment.md) |
| 15 | [04_setup_development_plan_6m.md](../04_setup_development_plan_6m.md) (риски, Фаза 2) |

## Сборка PPTX (как в `presentations/`)

Эталон: [`presentations/dvms_moscow/build_pptx.py`](../../../../../presentations/dvms_moscow/build_pptx.py).

```bash
# из папки presentation/
python -m pip install -r requirements.txt
python build_pptx.py                  # render mermaid (нужен Node.js) + build
python build_pptx.py --skip-mermaid   # без Node.js, если PNG уже в _assets/diagrams/
```

На Windows, где `python` — это Store-алиас, используйте лаунчер `py`:

```powershell
py -3 -m pip install -r requirements.txt
py -3 build_pptx.py
```

**Выход:** `DetMir_China_WFOE_Phase1.pptx` (15 слайдов, 16:9).

## Сборка HTML отчёта WFOE vs RO

```powershell
py -3 -m pip install markdown
py -3 build_wfoe_ro_tax_report_html.py
```

**Выход:** [wfoe-vs-ro-tax-report.html](./wfoe-vs-ro-tax-report.html) — sidebar с оглавлением, таблицы, mermaid (CDN), print-friendly CSS.

**Диаграммы.** Рендер в PNG:
1. **Node.js + npx** — локально через `@mermaid-js/mermaid-cli` (предпочтительно).
2. **Без Node.js** — автоматически через [mermaid.ink](https://mermaid.ink/) (нужен интернет).

PNG сохраняются рядом с `.mmd` в `_assets/diagrams/`. Флаг `--skip-mermaid` переиспользует уже готовые PNG без перерендера.

## Mermaid

- **Все диаграммы дека** — в [diagrams.md](./diagrams.md) (8 схем с описаниями и привязкой к слайдам).
- В Cursor / GitHub / GitLab блоки в `slides.md` и `diagrams.md` рендерятся автоматически.
- Для отдельного рендера — [Mermaid Live Editor](https://mermaid.live/) или файлы в `_assets/diagrams/`.
- Правила вёрстки (шрифт, `~~~` для вертикали в подграфах) — [`presentations/BASE_PROMPT.md`](../../../../../presentations/BASE_PROMPT.md), раздел 6.1.

## Статус

Драфт v1.0 · Текст и цифры синхронизированы с md-исследованием · `build_pptx.py` — к реализации по `build-spec.md`.
