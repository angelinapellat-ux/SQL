import mysql.connector

class StoreDB:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ditsiri",
            database="store"
        )
        self.cursor = self.db.cursor()

    def get_products(self):
        self.cursor.execute("""
            SELECT product.id, product.name, product.price, product.quantity, category.name
            FROM product
            JOIN category ON product.id_category = category.id
        """)
        return self.cursor.fetchall()

