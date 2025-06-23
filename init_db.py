import sqlite3

# Create or connect to sql.db
conn = sqlite3.connect("sql.db")
cursor = conn.cursor()

# Create employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    role TEXT,
    salary REAL,
    hire_date TEXT
)
""")

# Optional: Insert dummy data
cursor.executemany("""
INSERT INTO employees (name, role, salary, hire_date) VALUES (?, ?, ?, ?)
""", [
    ("Alice", "Engineer", 75000, "2022-03-10"),
    ("Bob", "Manager", 85000, "2021-06-22"),
    ("Charlie", "Analyst", 62000, "2023-01-15")
])

# Save and close
conn.commit()
conn.close()

print("✅ Database initialized with sample data.")
