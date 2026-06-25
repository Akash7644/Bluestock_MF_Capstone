import pandas as pd
import sqlite3

conn = sqlite3.connect("mutual_fund.db")

fund_df = pd.read_csv(r"D:\Bluestock\Project\Data\Raw\01_fund_master.csv")
nav_df = pd.read_csv(r"D:\Bluestock\Project\Data\Processed\clean_nav_history.csv")
transaction_df = pd.read_csv(r"D:\Bluestock\Project\Data\Processed\clean_transaction.csv")
performance_df = pd.read_csv(r"D:\Bluestock\Project\Data\Processed\clean_performance.csv")

fund_df["launch_date"] = pd.to_datetime(
    fund_df["launch_date"],
    errors="coerce"
).dt.strftime("%Y-%m-%d")

nav_df["date"] = pd.to_datetime(
    nav_df["date"],
    errors="coerce"
).dt.strftime("%Y-%m-%d")

transaction_df["transaction_date"] = pd.to_datetime(
    transaction_df["transaction_date"],
    errors="coerce"
).dt.strftime("%Y-%m-%d")

fund_df.to_sql(
    name="dim_fund",
    con=conn,
    if_exists="append",
    index=False
)

nav_df.to_sql(
    name="fact_nav",
    con=conn,
    if_exists="append",
    index=False
)

transaction_df.to_sql(
    name="fact_transactions",
    con=conn,
    if_exists="append",
    index=False
)

performance_df.to_sql(
    name="fact_performance",
    con=conn,
    if_exists="append",
    index=False
)

cursor = conn.cursor()

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    print(f"{table}: {cursor.fetchone()[0]} rows")

print("\nSample data:\n")

for table in tables:
    print(f"----- {table} -----")
    cursor.execute(f"SELECT * FROM {table} LIMIT 5")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print()

conn.commit()
conn.close()

print("All data successfully inserted into SQLite!")