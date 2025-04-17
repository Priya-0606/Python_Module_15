#Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data.

import sqlite3

dbcon = sqlite3.connect("student.db")

dbcon.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")
print("Table 'students' created successfully.")

result = dbcon.execute("SELECT COUNT(*) FROM students").fetchone()

count = result[0] if result else 0

if count == 0:
    dbcon.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Klaus", 20, "A"))
    dbcon.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Elijah", 22, "B"))
    dbcon.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Hope", 9, "A"))
    dbcon.commit()
    print("Data inserted successfully.")
else:
    print("Data already exists. Skipping insertion.")

rows = dbcon.execute("SELECT * FROM students").fetchall()

print("\nStudent Data:")
for row in rows:
    print("ID:", row[0], "| Name:", row[1], "| Age:", row[2], "| Grade:", row[3])

dbcon.close()
