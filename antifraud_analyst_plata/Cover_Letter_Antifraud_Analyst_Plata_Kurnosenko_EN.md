# Cover Letter – Antifraud Analyst Middle at Plata

**Vitaly Kurnosenko**  
Shanghai, China  
+86 15601694273 | vitaly@sinoptics.ai  
WeChat: porohnya | Skype: kurnosenko_vitaly  

---

**May 27, 2026**

**Hiring Team**  
Plata  
Serbia / Georgia

---

Dear Hiring Team,

I am writing to apply for the Antifraud Analyst Middle position at Plata.

For the past three years I have worked on an antifraud platform — Yofi/Botnot — that detects bot purchases, return fraud, discount abuse, reseller activity, and fake profiles for enterprise Shopify merchants. The work was hands-on: I maintained the fraud rules system, where all detection parameters were defined as per-client YAML configs and synchronized with dbt SQL macros for batch models. Tuning a threshold like `min_return_rate` or toggling a model on for a specific shop while keeping false positives under control is exactly the kind of work your job description describes.

On the ML side, I contributed to the scoring pipeline: a SageMaker-backed Lambda that runs each order through bot detection, discount abuse, and refund probability models, producing `is_bot_score`, trust/risk signals, and `is_bad_actor` decisions. I also extended the feature analytics service — shipping new return rate calculations and fuzzy pattern detection that fed both real-time scoring and back-testing via BigQuery and dbt. When rules needed back-testing, the data was already in the lake; the question was always how to slice it to get a meaningful signal without introducing hindsight bias.

I bring two things that are harder to teach than SQL or Python. First, a PhD in mathematical physics — probability theory and statistical modeling are not tools I read about, they are how I was trained to reason. Second, fifteen years of working inside the payment flows that fraud exploits: treasury operations, bank account management, card and transfer processes, BIN validation, compliance controls. Understanding *why* a transaction looks suspicious is easier when you understand how legitimate transactions are supposed to work.

What I find compelling about Plata specifically is the scope of the 2026 product expansion. New fraud scenarios across card, transfers, and tokenization channels are exactly the kind of problem where an analyst who has lived inside a rules-and-ML antifraud system can contribute from the first week rather than spending months on ramp-up.

I would be glad to discuss how my background fits the specific challenges your team is solving. Thank you for your consideration.

Sincerely,

**Vitaly Kurnosenko**

---

*Open to relocation to Serbia or Georgia; comfortable with remote arrangements.*
