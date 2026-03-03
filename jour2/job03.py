import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ditsiri",  
    database="LaPlateforme"
)

cursor = mydb.cursor()


# Ajout des données dans etage
cursor.execute("INSERT INTO etage (nom, numero, superficie) VALUES ('RDC', 0, 500)")
cursor.execute("INSERT INTO etage (nom, numero, superficie) VALUES ('R+1', 1, 500)")

# Ajout des données dans salle
cursor.execute("INSERT INTO salle (nom, id_etage, capacite) VALUES ('Lounge', 1, 100)")
cursor.execute("INSERT INTO salle (nom, id_etage, capacite) VALUES ('Studio Son', 1, 5)")
cursor.execute("INSERT INTO salle (nom, id_etage, capacite) VALUES ('Broadcasting', 2, 50)")
cursor.execute("INSERT INTO salle (nom, id_etage, capacite) VALUES ('Bocal Peda', 2, 4)")
cursor.execute("INSERT INTO salle (nom, id_etage, capacite) VALUES ('Coworking', 2, 80)")
cursor.execute("INSERT INTO salle (nom, id_etage, capacite) VALUES ('Studio Video', 2, 5)")

mydb.commit()  # Valide les insertions

for row in cursor.fetchall():
    print(row)

cursor.close()
mydb.close()
