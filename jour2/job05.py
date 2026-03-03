import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ditsiri",
    database="LaPlateforme"
)

cursor = mydb.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage")
result = cursor.fetchone()

superficie_totale = result[0]

print(f"La superficie de La Plateforme est de {superficie_totale} m2")

cursor.close()
mydb.close()
