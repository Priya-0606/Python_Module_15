#21) Write a Python program to create a database and a table using SQLite3.

import sqlite3

try:
    dbcon = sqlite3.connect("mydb.db")
    print("database is created succesfullly!")

    cur = dbcon.cursor()
    
except Exception as E:
    print(E)

#Create Table
create_tab = "create table student (Rollno INT PRIMARY KEY, Name VARCHAR(255),Branch VARCHAR(255))"

dbcon.commit()
dbcon.close()
