import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS stash_tracker")

print(db)