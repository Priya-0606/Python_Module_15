#22) Write a Python program to insert data into an SQLite3 database and fetch it.

import sqlite3

try:
    dbcon = sqlite3.connect("school.db")
    print("Database connected successfully!")

    dbcon.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
    """)
    print("Table 'students' created successfully.")

    dbcon.execute("""
    INSERT INTO students (name, age, grade)
    VALUES 
        ('Priya', 18, 'A'),
        ('Tanisha', 19, 'B'),
        ('Kruti', 17, 'A')
    """)
    dbcon.commit()
    print("Data inserted successfully.")

    rows = dbcon.execute("SELECT * FROM students").fetchall()

    print("\nStudent Data:")
    for row in rows:
        print("ID:", row[0], "| Name:", row[1], "| Age:", row[2], "| Grade:", row[3])

except Exception as e:
    print("Error:", e)

finally:
    dbcon.close()
