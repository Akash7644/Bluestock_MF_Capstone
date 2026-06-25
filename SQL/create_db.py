import sqlite3

conn = sqlite3.connect("mutual_fund.db")

with open("SQL/schema.sql", "r") as file:
    conn.executescript(file.read())

conn.commit()
conn.close()

print("Database and tables created successfully!")