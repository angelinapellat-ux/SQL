import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ditsiri",  
    database="LaPlateforme"
)

cursor = mydb.cursor()

# Création de la table etage
cursor.execute("""
CREATE TABLE etage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    numero INT,
    superficie INT
)
""")

# Création de la table salle
cursor.execute("""
CREATE TABLE salle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    id_etage INT,
    capacite INT,
    FOREIGN KEY (id_etage) REFERENCES etage(id)
)
""")

mydb.commit()  


for row in cursor.fetchall():
    print(row)

cursor.close()
mydb.close()
