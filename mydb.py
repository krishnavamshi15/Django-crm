import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Krishna@15"
)


cursor = db.cursor()

cursor.execute("use crm")
cursor.execute("drop table mydb")