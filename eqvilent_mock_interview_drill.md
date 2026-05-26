# Eqvilent Mock Interview Drill

Updated based on 41 real Glassdoor interview reviews. Structured by stage, not by a single 60-minute session, because Eqvilent's process is multi-stage and spread over weeks.

## How To Use This File

- Run each stage drill separately to match the actual process.
- First pass: answer freely, record yourself, do not stop.
- Second pass: tighten every answer to 60-90 seconds and hold the structure.
- Target tone: calm, precise, senior, hands-on. Do not apologize for the trading gap; map it to a fast ramp-up.

---

## Stage 1 Drill: HR Screening (30-45 min)

### Tell me about yourself.

I am a finance and operations professional based in Shanghai, with more than 15 years of experience in budgeting, treasury, cash-flow planning, management reporting, financial control, audit support, and cross-border operations. I have built finance processes from scratch, prepared budgets and plan-vs-actual analysis, managed payment planning and banking workflows, coordinated with auditors, and set up reporting logic in QAD/ERP.

At the same time, I have a practical technical profile. I use Python, SQL, workflow orchestration tools, and automation tools to process data and reduce manual work. My recent projects include document processing with OCR, Excel template automation, FastAPI services, PostgreSQL, Docker/K3s, Celery/Redis, and cloud deployment.

This role is especially interesting because it combines finance operations, trading data analysis, reconciliations, Python, and workflow automation. That is exactly the direction I want to develop in.

---

### Why Eqvilent?

Three reasons. First, the role itself combines finance, trading data, Python, reconciliations, and automation - exactly the intersection I want to develop in. Second, the company culture: technically strong, remote-first, fast feedback loops, and serious investment in infrastructure and people. Third, the long-term direction: a growing quant trading firm with global presence creates strong learning and growth potential for someone who wants to stay hands-on with data and finance.

---

### Why this role if you have CFO experience?

For me the title is less important than the content and environment. I am interested in hands-on data and process work in a strong quant trading company. My senior finance background is useful as context - I understand financial controls, governance, reporting quality, and stakeholder expectations. But I am very comfortable doing the detailed work directly: cleaning data, checking exceptions, writing scripts, building reports. This is actually the kind of work I find most satisfying.

---

### What are your salary expectations?

Given the hybrid nature of the role - finance operations, trading data analysis, Python-based reporting, reconciliations, and workflow automation - my expected range would be around USD 90,000-105,000 gross annually. The final number depends on the scope, seniority level, bonus structure, and overall benefits package.

---

### How comfortable are you with NDA?

I am comfortable with NDA. I treat confidentiality as part of professional standards, especially in finance and trading. I would just like to review the document properly before signing, which I assume is the standard process. For non-compete, I am open to discussing terms proportional to the role and the probation period.

---

### Are you comfortable working fully remote with a global team?

Yes. I have been managing international operations in China for more than 15 years, working with Russian and Chinese founders, banks, auditors, and management across time zones. I am very comfortable with structured written communication, async work, video calls across time zones, and self-managed deadlines. Remote is not a limitation for me - it is a working style I am already used to.

---

### What do you know about the company?

Eqvilent is an international quantitative trading firm with strong technical infrastructure, a remote-first culture, and global presence in Dubai, London, Lisbon, Mumbai, and Malta. The company has over 2,000 GPUs, 31,000+ CPU cores, and 1.5 PB of RAM. They emphasize precision, intellectual work, and strong teams - including Kaggle Grandmasters. The finance function in such a company is closer to data and operations than to classical accounting, which is exactly what makes this role interesting.

---

### Questions to ask HR

1. Could you walk me through the next stages of the process and typical timelines?
2. What does the Finance Team look like today - size, structure, and who I would work with directly?
3. What Python and workflow tools does the team currently use?

---

## Stage 2 Preparation: Take-Home Assignment

This is not a drill but a preparation checklist for when you receive the assignment.

### Before starting

- Read the assignment fully twice before opening Python.
- Note what is being assessed: accuracy, code quality, business reasoning, or communication.
- Clarify deadline and submission format if not specified.
- Ask whether external libraries are permitted.

### During execution

- Sketch the data map first: fields, types, value ranges, edge cases.
- Preserve raw source data unchanged.
- Document every assumption: "I assumed X because Y."
- Structure: normalize → validate → match → classify exceptions → summary.
- Deliver an Excel report with multiple sheets: raw, cleaned, exceptions, summary.
- Write a README of 1-2 pages: assumptions, methodology, results, limitations.

### After completion

- Re-read the README after one hour with fresh eyes.
- Verify the script runs from a clean environment.
- Submit as a ZIP with clear folder structure.

### If the task takes longer than expected

Do less, but do it well. A thoughtful, documented partial solution beats a rushed complete one.

---

## Stage 3 Drill: Technical Interview On Assignment

### Walk me through your approach to the assignment.

I started by reading the assignment twice and mapping the data: field names, types, value ranges, and obvious edge cases. Then I preserved the raw data unchanged and normalized both datasets: column names, date formats, time zones, currencies, and numeric precision.

For matching I used trade ID where available. Where it was missing or unreliable I built a composite key. After matching I classified exceptions into two categories: completeness breaks (missing on one side) and value breaks (quantity, price, fee, currency, settlement date differences). I separated them intentionally because the investigation path is different.

The output was a multi-sheet Excel file with raw data, cleaned data, exception report, and a summary by broker and asset class.

---

### What would you do differently with more time?

I would add composite-key matching for cases where trade ID is missing. I would add a fee schedule lookup to validate whether broker-reported fees match expected fees based on exchange, asset class, and quantity. I would also add daily scheduling and alerting so the reconciliation runs automatically and flags only material breaks.

---

### What edge cases did you handle, or should have handled?

Timezone differences between systems. Instrument identifier inconsistencies - same instrument named differently by broker and internally. Aggregation differences - broker may report at daily level while internal data is trade-level. Rounding and currency precision differences in fee comparison. Duplicate trades with slightly different timestamps.

---

### How would you scale this to process millions of trades daily?

Move from a pandas notebook to a proper pipeline. Use a database (PostgreSQL or similar) to store raw, normalized, and exception data with proper indexing. Replace file-based ingestion with API polling or message queue. Add incremental processing instead of full reloads. Schedule via Airflow or a similar orchestrator. Monitor data quality metrics and alert thresholds rather than reviewing every exception manually.

---

### Basic pandas questions to prepare

```python
# Merge with indicator
merged = internal.merge(broker, on="trade_id", how="outer", indicator=True)

# Find missing on each side
missing_internal = merged[merged["_merge"] == "right_only"]
missing_broker   = merged[merged["_merge"] == "left_only"]

# Variance column
matched["fee_diff"] = matched["fee_internal"] - matched["fee_broker"]

# Group summary
summary = matched.groupby(["broker", "asset_class"]).agg(
    trades=("trade_id", "count"),
    total_fee_diff=("fee_diff", "sum"),
    breaks=("fee_diff", lambda s: (s.abs() > 0.01).sum()),
).reset_index()

# Flag tolerance breach
exceptions = matched[matched["fee_diff"].abs() > 0.01]
```

---

## Stage 4 Drill: Hiring Manager Interview (Finance)

### Tell me about a finance process you built from scratch.

At Shanghai Nine-Two-Nine Aircraft Design Limited Company I launched the finance function from zero for an international team of ten people in China. There were no procedures, no payment controls, no budgeting framework, nothing.

I designed procurement and contract approval procedures, payment limits, budgeting rules, cash-flow scenario templates, and reporting materials for the board. I coordinated with banks, auditors, Russian and Chinese founders, and management. I also set up document control and approval workflows.

The result was a controlled finance operating model: payments went through approval, budget deviations were tracked, auditors had structured documentation, and management had visibility into cash positions and spending. This maps directly to what Eqvilent needs: process design, finance operations, controls, and workflow structure.

---

### How do you ensure accuracy in financial data?

I start with source control: where the data comes from, who owns it, and whether raw data is preserved and immutable. Then I define a consistent structure: dates, currencies, entities, accounts, categories, and responsible owners. After that I apply reconciliation checks, variance thresholds, duplicate checks, missing-value checks, and approval logic. Finally, I make the output explainable: a summary report with material variances highlighted, a detailed exception list, and clear ownership of each break.

For broker and exchange data I would apply the same pattern: preserve raw, normalize, match, classify exceptions, produce report, automate.

---

### Describe your plan-vs-actual analysis approach.

Plan-vs-actual is not only comparing numbers. I start by defining the structure: period, department, cost category, project, entity, currency, and responsible owner. Then I compare actuals against budget and flag material variances. I classify variances by type: timing, price, volume, FX, one-off, structural change, or data issue. Each type needs a different response: update the forecast, control spending, investigate the data, or adjust assumptions. The final step is to produce a report that gives management a clear picture and actionable next steps.

---

### What automation would you build first for the Finance Team?

I would start by mapping the current manual workflow and identifying the highest-frequency repeated steps. Usually the first good target is data ingestion and normalization: pulling broker and exchange files or API data, standardizing the schema, and producing a reliable clean input dataset. The second target is the reconciliation check and exception report itself. The third is alerting and scheduling so the report runs daily without manual trigger and only escalates material breaks.

Before automating anything, I would make sure the logic is correct, documented, and explainable. A fast wrong process is worse than a slower controlled one.

---

## Stage 5 Drill: Behavioral / Culture Interview

### Tell me about the most challenging project you worked on.

Building the finance function from scratch at Shanghai Nine-Two-Nine was probably the most complex because there was no precedent, no documentation, and no existing process to refer to. I had to design everything: approval flows, payment controls, budgeting framework, cash-flow reporting, audit preparation, and board materials, all simultaneously, while also managing day-to-day operations.

The challenge was not technical. It was holding the structure together when everything was new, the team was international, the legal environment was Chinese, and the founders had different expectations. What worked was starting with the highest-risk areas first (payment controls, audit documentation) and building outward from there.

The result was a functional finance operating model that passed an external audit in its first year of operation.

---

### Describe complex cases you handled and how you approached them.

One example: we had a situation where cash-flow projections showed a potential liquidity shortfall in a specific month, but the underlying data came from three different systems with inconsistent categorizations. Management needed a clear answer quickly.

I stopped trying to reconcile the systems automatically and instead mapped each data source manually, identified where the inconsistencies were, and rebuilt the projection from verified inputs. I documented each assumption and presented two scenarios to management: conservative and base case, with the key variables identified. Management made the decision within a day.

The lesson: when data is unreliable, the answer is not to ignore the problem - it is to make the uncertainty explicit and give decision-makers a structured view.

---

### Why are you looking for a new role?

I am looking for a more technical and data-driven finance environment. My recent roles were strong on finance operations, management reporting, and cross-border coordination. But I want to focus more on data, Python, automation, and modern finance workflows. Eqvilent is exactly the type of company where finance, data, and trading operations come together in a technically serious environment.

---

### Tell me about a time you led a project end to end.

At CRAIC I led the annual budgeting and quarterly reporting cycle for several years. This meant coordinating inputs from multiple departments, reconciling them against prior period actuals, building cash-flow scenarios, preparing management materials, and presenting to the board.

The key challenge was that the data came from different sources - accounting, operations, procurement - and each team had its own format and timeline. I created a standard template structure, set firm data collection deadlines, and built a validation layer that flagged inconsistencies before the data was used.

The result was a faster, more reliable process that reduced last-minute corrections significantly.

---

### How do you handle disagreements with stakeholders?

I start by understanding their position fully before responding. Usually disagreements come from different information, different priorities, or different risk tolerance - not from bad intentions. I try to separate the factual disagreement from the relationship and present the data clearly without making it personal.

In finance, I have found that most disagreements resolve when you show the underlying data transparently, acknowledge the other person's constraint, and propose a way forward that addresses the core concern. If we genuinely disagree after that, I escalate to the appropriate level and document the discussion.

---

## Stage 6 Drill: Top Management / CEO Interview

### What would you bring to the Finance Team that is not already there?

The combination of senior finance discipline and hands-on technical execution. Many finance professionals understand controls and reporting but rely on others for data work. I can close that gap: I can design the control logic and also write the Python that implements it, connect it to the data source, and automate the reporting. That means faster iteration and less dependency on engineering resources for finance-specific workflows.

---

### Where do you want to be in three years?

I want to be a strong contributor at the intersection of finance and data in a technically serious environment. Specifically, I want to have built reliable reconciliation and reporting infrastructure for Finance, developed domain expertise in trading data, and grown into ownership of the finance data workflow end to end. I am not looking to move into management quickly. I would rather deepen the technical and analytical side for now.

---

### What question do you have about the company at the CEO level?

How does the Finance Team fit into the broader data infrastructure of the firm? Specifically, are reconciliations and finance data pipelines part of a shared data platform, or does Finance operate its own stack? And as the firm scales across more exchanges and asset classes, what is the biggest data quality challenge the Finance Team faces today?

---

## Final Closing Statement (All Stages)

Thank you for the conversation. The role is even more interesting to me after this discussion because it sits exactly at the intersection I am looking for: finance operations, trading data, Python automation, and process improvement. I believe I can bring strong financial discipline and hands-on technical execution, while ramping up quickly on your specific broker and exchange data flows.
