-- 1. Top 5 Funds by AUM
SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV per Month
SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 3. SIP Inflow Year-over-Year
SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip_inflow
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;


-- 4. Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 5. Funds with Expense Ratio Less Than 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- 6. Top 10 Funds by 5-Year Return
SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- 7. Average Sharpe Ratio by Category
SELECT
    category,
    ROUND(AVG(sharpe_ratio), 2) AS avg_sharpe_ratio
FROM fact_performance
GROUP BY category
ORDER BY avg_sharpe_ratio DESC;


-- 8. Total Investment by Payment Mode
SELECT
    payment_mode,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_investment DESC;


-- 9. Average NAV for Each Fund
SELECT
    amfi_code,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY average_nav DESC;


-- 10. Top 5 States by Investment Amount
SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 5;