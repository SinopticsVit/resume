В mature environments reconciliation состоит из:
Stage	Что происходит
Detection	Найти mismatch
Classification	Понять тип
Investigation	Найти root cause
Resolution	Исправить
Prevention	Автоматизировать / убрать источник

Что делает сильный analyst
Он пытается понять:
почему появляются ложные breaks?
И потом:
улучшает matching logic  
добавляет tolerance rules
учитывает broker behavior
автоматизирует classification

Поэтому ценится analyst, который умеет:
Навык	Почему важен
Understand trade lifecycle	Понимать, что реально происходит
Detect patterns	Видеть recurring breaks
Improve reconciliation logic	Уменьшать noise
Automate exception handling	Снижать ручную работу
Separate noise from real risk	Выделять настоящие проблемы


Что ценится в analyst
Умение:
понимать fee models
понимать exchange economics
замечать неправильный tier
автоматизировать fee validation
объяснять unexplained fee spikes



Какие fees входят
Fee	Что это
Commission	Комиссия брокера
Exchange fee	Fee биржи
Clearing fee	Clearing house
Regulatory fee	SEC/FINRA/etc


## 7. Trading Vocabulary

### Core Terms

- **Order:** instruction to buy or sell an instrument.
- **Trade / execution:** completed transaction.
- **Fill:** partial or full execution of an order.
- **Position:** current holding after trades net.
- **Asset class:** category of instruments: equities, futures, options, FX, crypto, fixed income.
- **Broker:** intermediary that executes or clears trades.
- **Exchange:** marketplace where instruments are traded.
- **Clearing:** post-trade process confirming obligations between parties.
- **Settlement:** final transfer of cash and assets.
- **Commission:** broker charge per trade.
- **Exchange fee:** fee charged by the exchange itself.
- **PnL:** profit and loss.
- **Margin:** collateral required to support open positions.
- **Collateral:** assets pledged to cover exposure.

### Common Data Sources

- Broker statements.
- Exchange reports.
- Internal trade logs.
- Clearing reports.
- Bank and cash statements.
- Fee schedules.
- Market and reference data.

### Typical Reconciliation Breaks

- Trade exists internally but missing at broker.
- Trade exists at broker but missing internally.
- Duplicate trade.
- Quantity mismatch.
- Price mismatch.
- Fee or commission mismatch.
- Wrong currency.
- Timezone or timestamp issue.
- Settlement date mismatch.
- Instrument identifier mismatch.
- Aggregation mismatch: trade-level vs daily summary.




### Question: How would you reconcile internal trading data with broker or exchange data?
clarify the reconciliation objective: trade completeness, fee validation, cash movement, position reconciliation, or PnL support. Then I would identify the data sources and define the common schema: trade ID, instrument, broker, exchange, side, quantity, price, currency, trade timestamp, settlement date, fees, and account.

Next I would normalize both datasets: column names, date formats, time zones, currency codes, instrument identifiers, and numeric precision. Then define the matching logic. If a reliable trade ID exists, use it. If not, build a composite key using instrument, side, quantity, price, timestamp bucket, broker, and account.

After matching, classify exceptions:

- missing internally;
- missing at broker;
- price or quantity difference;
- fee difference;
- currency or FX issue;
- settlement date issue;
- duplicate or aggregation issue.

For reporting, produce a summary by broker, exchange, asset class, date, and severity, plus a detailed exception list for investigation. Then automate so repeated reconciliations run identically every day and alerts fire only for material breaks.


## 10. Questions To Ask Them
### Role scope
- What are the main data sources: brokers, exchanges, internal systems, databases, files, or APIs?
- Is the role more focused on recurring reconciliations, ad hoc analytics, or process automation?
- What are the most painful finance workflows today?
- What does success look like after 3 and 6 months?