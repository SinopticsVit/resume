# Спецификация для генерации PPTX (`build_pptx.py`)

> Источник контента: [slides.md](./slides.md)  
> Эталон сборщика: [`presentations/dvms_moscow/build_pptx.py`](../../../../../presentations/dvms_moscow/build_pptx.py)  
> Диаграммы: `_assets/diagrams/*.mmd` → PNG через `npx @mermaid-js/mermaid-cli` или fallback `mermaid.ink`

## Параметры дека

| Параметр | Значение |
|---|---|
| `OUTPUT_PPTX` | `DetMir_China_WFOE_Phase1.pptx` |
| `SLIDE_W` | 13.333 in (16:9) |
| `SLIDE_H` | 7.5 in |
| `FONT_TITLE` | Georgia или Segoe UI Semibold |
| `FONT_BODY` | Segoe UI |
| `DECK_LABEL` | «Детский Мир · WFOE КНР · Фаза 1» |
| `MERMAID_FONT` | Segoe UI, fontSize 18–20px; для CN-нод — Microsoft YaHei |

## Реестр диаграмм

| diagram_id | Файл `.mmd` | Слайд | layout | Примечание |
|---|---|---:|---|---|
| `func-blocks` | `diagram-01-func-blocks.mmd` | 4 | `diagram_right` | Карта F1–F10; справа, слева — легенда |
| `org-structure` | `diagram-02-org-structure.mmd` | 6 | `diagram_full` | Оргсхема; пунктир = функциональные связи |
| `budget-flow` | `diagram-03-budget-flow.mmd` | 9 | `diagram_full` | Cost-plus потоки денег |
| `roadmap-phases` | `diagram-04-roadmap-phases.mmd` | 11 | `diagram_top` | Фазы 0→1→2→оценка |
| `moscow-links` | `diagram-05-moscow-links.mmd` | 13 | `diagram_full` | Горизонтальные связи |
| `process-samples` | `diagram-06-process-samples.mmd` | 14 | `two_column` | Левая половина слайда |
| `process-qc` | `diagram-07-process-qc.mmd` | 14 | `two_column` | Правая половина слайда |
| `sample-payment` | `diagram-08-sample-payment.mmd` | 14 | `diagram_bottom` | Под двумя процессами, компактно |

### Порядок извлечения mermaid из `slides.md`

Блоки mermaid в `slides.md` идут **в том же порядке**, что `diagram-01` … `diagram-08`. Сборщик может:

1. Парсить ` ```mermaid ` из `slides.md` regex-ом (как в dvms_moscow), **или**
2. Читать готовые `.mmd` из `_assets/diagrams/` (рекомендуется — проще diff).

## Реестр таблиц

| table_id | Слайд | layout | Колонки | Строк данных | Стиль |
|---|---:|---|---|---|---|
| `scope-in-out` | 3 | `two_column_bullets` | «В scope» / «Out of scope» | 6 + 5 | Левая колонка teal, правая muted |
| `functions-summary` | 5 | `table_full` | Функция · Цель · KPI (кратко) | 5 (F1–F5) | Header navy, zebra rows |
| `team-locations` | 7 | `table_compact` | Локация · Роли · Чел. | 3 | Accent на строке «Итого» |
| `budget-summary` | 8 | `table_full` | Блок · CNY · RUB (×12) | 4 + run-rate | Числа right-align |
| `service-contracts` | 10 | `table_full` | Услуга · Функция · Модель оплаты | 7 | 7 строк + примечание в footer |
| `roadmap-months` | 11 | `table_below_diagram` | Месяц · Ключевые действия · Веха | 6 (M1–M6) | M4/M5 highlight |
| `milestones` | 12 | `table_compact` | # · Веха · Срок | 13 | Нумерация 1–13 |
| `kpi-phases` | 12 | `table_right_or_below` | KPI · M1–M2 · M3–M4 · M5–M6 | 8 | 3 фазы |
| `hiring-ramp` | 12 | `table_compact` | Роль · M1…M6 (●) | 13 | Dot matrix, как в 03_budget |
| `sla` | 15 | `table_two_col` | Параметр · Значение | 9 | Компактный шрифт 13pt |
| `phase2-criteria` | 15 | `checklist` | Критерий · Статус ☐ | 5 | Чекбоксы для go/no-go |

## Карта слайдов → функции Python

Каждый слайд — отдельная функция `slide_NN_*` в `build_pptx.py`. Структура данных:

```python
SLIDES = [
    {
        "id": 1,
        "layout": "title",
        "title": "...",
        "subtitle_lines": [...],
        "footer": "...",
        "notes": "...",
    },
    {
        "id": 4,
        "layout": "header_diagram_legend",
        "title": "Карта функциональных блоков",
        "diagram_id": "func-blocks",
        "bullets": [...],  # легенда F1-F10
        "notes": "...",
    },
    # ...
]
```

### Layout types

| layout | Описание | Helper в Python |
|---|---|---|
| `title` | Титул, navy bar + crimson accent | `_title_slide()` |
| `header_bullets` | Стандартный header + bullets | `_header_bar()` + `_bullets()` |
| `header_diagram_legend` | Header + diagram справа + bullets слева | `_photo_or_diagram()` |
| `diagram_full` | Header + diagram на всю ширину | `_embed_diagram()` |
| `diagram_top` | Diagram сверху, table снизу | `_embed_diagram()` + `_native_table()` |
| `table_full` | Header + нативная PPTX-таблица | `_native_table()` |
| `two_column` | Два столбца (bullets или mini-diagram) | `_two_columns()` |
| `two_column_bullets` | Две колонки буллетов (scope) | `_two_columns()` |
| `closing` | Финал: тезис + CTA | `_closing_slide()` |

## Цветовые токены (скопировать в `build_pptx.py`)

```python
NAVY = RGBColor(0x1B, 0x2A, 0x4A)
TEAL = RGBColor(0x1A, 0x7A, 0x6D)
CRIMSON = RGBColor(0xB0, 0x2A, 0x30)
GOLD = RGBColor(0xC8, 0x96, 0x2E)
BG_IVORY = RGBColor(0xFA, 0xF8, 0xF5)
TABLE_HEADER_BG = NAVY
TABLE_ROW_EVEN = RGBColor(0xF2, 0xEF, 0xEB)
TABLE_ROW_ODD = BG_IVORY
```

## CLI сборщика (рекомендуемый)

```bash
python -m pip install python-pptx
python build_pptx.py                  # render mermaid + build
python build_pptx.py --skip-mermaid   # только PPTX из кэша PNG
```

## Зависимости

```
python-pptx>=0.6.23
# для mermaid: Node.js + npx @mermaid-js/mermaid-cli
```
