# Data Dictionary

## Project: Mutual Fund Data Warehouse (SQLite)

This document describes the schema, data types, business definitions, and source references for all tables used in the Mutual Fund Data Warehouse.

---

# 1. Dimension Table: `dim_fund`

**Source File:** `Data/Raw/01_fund_master.csv`

| Column             | Data Type | Business Definition                                                             |
| ------------------ | --------- | ------------------------------------------------------------------------------- |
| amfi_code          | INTEGER   | Unique AMFI identifier assigned to each mutual fund scheme.                     |
| fund_house         | TEXT      | Name of the Asset Management Company (AMC).                                     |
| scheme_name        | TEXT      | Official name of the mutual fund scheme.                                        |
| category           | TEXT      | Broad category of the mutual fund (Equity, Debt, Hybrid, etc.).                 |
| sub_category       | TEXT      | Detailed investment category within the fund category.                          |
| plan               | TEXT      | Investment plan (Regular or Direct).                                            |
| launch_date        | DATE      | Date on which the scheme was launched.                                          |
| benchmark          | TEXT      | Benchmark index used to evaluate fund performance.                              |
| expense_ratio_pct  | REAL      | Annual fund management expense charged to investors (%).                        |
| exit_load_pct      | REAL      | Exit load charged when redeeming units before the specified holding period (%). |
| min_sip_amount     | INTEGER   | Minimum investment amount allowed through SIP (₹).                              |
| min_lumpsum_amount | INTEGER   | Minimum one-time investment amount (₹).                                         |
| fund_manager       | TEXT      | Name of the fund manager responsible for managing the scheme.                   |
| risk_category      | TEXT      | Risk classification assigned to the scheme.                                     |
| sebi_category_code | TEXT      | SEBI classification code for the mutual fund scheme.                            |

---

# 2. Fact Table: `fact_nav`

**Source File:** `Data/Processed/clean_nav_history.csv`

| Column    | Data Type | Business Definition                               |
| --------- | --------- | ------------------------------------------------- |
| amfi_code | INTEGER   | AMFI scheme code linking NAV history to the fund. |
| date      | DATE      | Date on which NAV was recorded.                   |
| nav       | REAL      | Net Asset Value per unit on the given date.       |

---

# 3. Fact Table: `fact_transactions`

**Source File:** `Data/Processed/clean_transaction.csv`

| Column             | Data Type | Business Definition                                   |
| ------------------ | --------- | ----------------------------------------------------- |
| investor_id        | TEXT      | Unique identifier for the investor.                   |
| transaction_date   | DATE      | Date of the investment transaction.                   |
| amfi_code          | INTEGER   | AMFI code of the mutual fund scheme.                  |
| transaction_type   | TEXT      | Type of transaction (SIP, Lumpsum, Redemption, etc.). |
| amount_inr         | INTEGER   | Transaction amount in Indian Rupees (₹).              |
| state              | TEXT      | State of the investor.                                |
| city               | TEXT      | City of the investor.                                 |
| city_tier          | TEXT      | Classification of the city (Tier 1, Tier 2, Tier 3).  |
| age_group          | TEXT      | Investor age category.                                |
| gender             | TEXT      | Gender of the investor.                               |
| annual_income_lakh | REAL      | Annual income of the investor (in lakhs).             |
| payment_mode       | TEXT      | Payment method used for the transaction.              |
| kyc_status         | TEXT      | Investor KYC verification status.                     |

---

# 4. Fact Table: `fact_performance`

**Source File:** `Data/Processed/clean_performance.csv`

| Column             | Data Type | Business Definition                                             |
| ------------------ | --------- | --------------------------------------------------------------- |
| amfi_code          | INTEGER   | AMFI scheme identifier.                                         |
| scheme_name        | TEXT      | Name of the mutual fund scheme.                                 |
| fund_house         | TEXT      | Asset Management Company (AMC).                                 |
| category           | TEXT      | Mutual fund category.                                           |
| plan               | TEXT      | Investment plan (Regular/Direct).                               |
| return_1yr_pct     | REAL      | Annualized return over the last 1 year (%).                     |
| return_3yr_pct     | REAL      | Annualized return over the last 3 years (%).                    |
| return_5yr_pct     | REAL      | Annualized return over the last 5 years (%).                    |
| benchmark_3yr_pct  | REAL      | Three-year benchmark return (%).                                |
| alpha              | REAL      | Alpha indicating excess return over the benchmark.              |
| beta               | REAL      | Beta measuring fund volatility relative to the market.          |
| sharpe_ratio       | REAL      | Risk-adjusted return using the Sharpe Ratio.                    |
| sortino_ratio      | REAL      | Downside risk-adjusted return using the Sortino Ratio.          |
| std_dev_ann_pct    | REAL      | Annualized standard deviation representing fund volatility (%). |
| max_drawdown_pct   | REAL      | Maximum observed decline from peak NAV (%).                     |
| aum_crore          | INTEGER   | Assets Under Management (AUM) in crore rupees.                  |
| expense_ratio_pct  | REAL      | Annual expense ratio charged by the fund (%).                   |
| morningstar_rating | INTEGER   | Morningstar rating assigned to the scheme (1–5).                |
| risk_grade         | TEXT      | Overall investment risk grade assigned to the scheme.           |

---

# Source References

| Table             | Source File                          |
| ----------------- | ------------------------------------ |
| dim_fund          | Data/Raw/01_fund_master.csv          |
| fact_nav          | Data/Processed/clean_nav_history.csv |
| fact_transactions | Data/Processed/clean_transaction.csv |
| fact_performance  | Data/Processed/clean_performance.csv |

---

# Notes

* Database: SQLite
* Schema Type: Star Schema
* Primary Business Key: `amfi_code`
* Date Format: `YYYY-MM-DD`
* Currency: Indian Rupees (INR)
* Data cleaning included handling missing values, data type standardization, validation, and formatting before loading into SQLite.
