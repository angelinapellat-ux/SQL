import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ditsiri",  
    database="LaPlateforme"
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM etudiant")

for row in cursor.fetchall():
    print(row)

cursor.close()
mydb.close()
