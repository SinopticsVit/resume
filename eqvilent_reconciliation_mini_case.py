"""Mini-case for Eqvilent Analyst interview preparation.

The script creates two small trading datasets, reconciles them, classifies
exceptions, and writes an Excel report that can be discussed in an interview.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


OUTPUT_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = OUTPUT_DIR / "eqvilent_reconciliation_report.xlsx"


def build_sample_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    internal = pd.DataFrame(
        [
            {
                "trade_id": "T001",
                "trade_date": "2026-05-08",
                "broker": "BrokerA",
                "exchange": "CME",
                "asset_class": "Futures",
                "instrument": "ESM6",
                "side": "BUY",
                "quantity": 10,
                "price": 5250.25,
                "currency": "USD",
                "fee": 12.50,
            },
            {
                "trade_id": "T002",
                "trade_date": "2026-05-08",
                "broker": "BrokerA",
                "exchange": "CME",
                "asset_class": "Futures",
                "instrument": "NQM6",
                "side": "SELL",
                "quantity": 5,
                "price": 18320.50,
                "currency": "USD",
                "fee": 8.25,
            },
            {
                "trade_id": "T003",
                "trade_date": "2026-05-08",
                "broker": "BrokerB",
                "exchange": "LSE",
                "asset_class": "Equity",
                "instrument": "ABC.L",
                "side": "BUY",
                "quantity": 1000,
                "price": 4.21,
                "currency": "GBP",
                "fee": 6.00,
            },
            {
                "trade_id": "T004",
                "trade_date": "2026-05-08",
                "broker": "BrokerC",
                "exchange": "Binance",
                "asset_class": "Crypto",
                "instrument": "BTCUSDT",
                "side": "BUY",
                "quantity": 1,
                "price": 64500.00,
                "currency": "USDT",
                "fee": 25.00,
            },
            {
                "trade_id": "T005",
                "trade_date": "2026-05-08",
                "broker": "BrokerB",
                "exchange": "Eurex",
                "asset_class": "Options",
                "instrument": "DAX-C-19000",
                "side": "SELL",
                "quantity": 20,
                "price": 31.10,
                "currency": "EUR",
                "fee": 10.00,
            },
        ]
    )

    broker = pd.DataFrame(
        [
            # Exact match.
            {
                "trade_id": "T001",
                "trade_date": "2026-05-08",
                "broker": "BrokerA",
                "exchange": "CME",
                "asset_class": "Futures",
                "instrument": "ESM6",
                "side": "BUY",
                "quantity": 10,
                "price": 5250.25,
                "currency": "USD",
                "fee": 12.50,
            },
            # Fee mismatch.
            {
                "trade_id": "T002",
                "trade_date": "2026-05-08",
                "broker": "BrokerA",
                "exchange": "CME",
                "asset_class": "Futures",
                "instrument": "NQM6",
                "side": "SELL",
                "quantity": 5,
                "price": 18320.50,
                "currency": "USD",
                "fee": 9.75,
            },
            # Quantity mismatch.
            {
                "trade_id": "T003",
                "trade_date": "2026-05-08",
                "broker": "BrokerB",
                "exchange": "LSE",
                "asset_class": "Equity",
                "instrument": "ABC.L",
                "side": "BUY",
                "quantity": 900,
                "price": 4.21,
                "currency": "GBP",
                "fee": 6.00,
            },
            # T004 missing from broker side.
            # T006 missing from internal side.
            {
                "trade_id": "T006",
                "trade_date": "2026-05-08",
                "broker": "BrokerD",
                "exchange": "NYSE",
                "asset_class": "Equity",
                "instrument": "XYZ",
                "side": "SELL",
                "quantity": 200,
                "price": 112.40,
                "currency": "USD",
                "fee": 5.25,
            },
            # Currency mismatch.
            {
                "trade_id": "T005",
                "trade_date": "2026-05-08",
                "broker": "BrokerB",
                "exchange": "Eurex",
                "asset_class": "Options",
                "instrument": "DAX-C-19000",
                "side": "SELL",
                "quantity": 20,
                "price": 31.10,
                "currency": "USD",
                "fee": 10.00,
            },
        ]
    )

    return internal, broker


def normalize(df: pd.DataFrame) -> pd.DataFrame:
    normalized = df.copy()
    normalized["trade_date"] = pd.to_datetime(normalized["trade_date"])
    for column in ("quantity", "price", "fee"):
        normalized[column] = pd.to_numeric(normalized[column])
    for column in ("broker", "exchange", "asset_class", "instrument", "side", "currency"):
        normalized[column] = normalized[column].str.strip().str.upper()
    return normalized


def classify_exception(row: pd.Series) -> str:
    if row["_merge"] == "left_only":
        return "Missing in broker statement"
    if row["_merge"] == "right_only":
        return "Missing in internal trade log"

    issues: list[str] = []
    if abs(row["quantity_internal"] - row["quantity_broker"]) > 0:
        issues.append("Quantity mismatch")
    if abs(row["price_internal"] - row["price_broker"]) > 0.01:
        issues.append("Price mismatch")
    if abs(row["fee_internal"] - row["fee_broker"]) > 0.01:
        issues.append("Fee mismatch")
    if row["currency_internal"] != row["currency_broker"]:
        issues.append("Currency mismatch")
    return "; ".join(issues) if issues else "OK"


def reconcile(internal: pd.DataFrame, broker: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    merged = internal.merge(
        broker,
        on="trade_id",
        how="outer",
        suffixes=("_internal", "_broker"),
        indicator=True,
    )

    merged["exception_type"] = merged.apply(classify_exception, axis=1)
    exceptions = merged[merged["exception_type"] != "OK"].copy()

    matched = merged[merged["_merge"] == "both"].copy()
    matched["fee_diff"] = matched["fee_internal"] - matched["fee_broker"]
    matched["quantity_diff"] = matched["quantity_internal"] - matched["quantity_broker"]
    matched["price_diff"] = matched["price_internal"] - matched["price_broker"]

    summary = (
        matched.groupby(["broker_internal", "asset_class_internal"], dropna=False)
        .agg(
            trades=("trade_id", "count"),
            internal_fee=("fee_internal", "sum"),
            broker_fee=("fee_broker", "sum"),
            fee_diff=("fee_diff", "sum"),
            quantity_breaks=("quantity_diff", lambda s: int((s != 0).sum())),
            price_breaks=("price_diff", lambda s: int((s.abs() > 0.01).sum())),
        )
        .reset_index()
        .rename(
            columns={
                "broker_internal": "broker",
                "asset_class_internal": "asset_class",
            }
        )
    )

    return exceptions, summary


def main() -> None:
    internal_raw, broker_raw = build_sample_data()
    internal = normalize(internal_raw)
    broker = normalize(broker_raw)
    exceptions, summary = reconcile(internal, broker)

    with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl") as writer:
        internal.to_excel(writer, index=False, sheet_name="internal_trades")
        broker.to_excel(writer, index=False, sheet_name="broker_statement")
        exceptions.to_excel(writer, index=False, sheet_name="exceptions")
        summary.to_excel(writer, index=False, sheet_name="summary")

    print(f"Created reconciliation report: {OUTPUT_PATH}")
    print("\nException summary:")
    print(exceptions[["trade_id", "_merge", "exception_type"]].to_string(index=False))


if __name__ == "__main__":
    main()

