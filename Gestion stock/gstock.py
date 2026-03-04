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

    def add_product(self, name, description, price, quantity, id_category):
        self.cursor.execute("""
            INSERT INTO product (name, description, price, quantity, id_category)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, description, price, quantity, id_category))
        self.db.commit()

    def delete_product(self, product_id):
        self.cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
        self.db.commit()

    def update_product(self, product_id, name, price, quantity):
        self.cursor.execute("""
            UPDATE product
            SET name=%s, price=%s, quantity=%s
            WHERE id=%s
        """, (name, price, quantity, product_id))
        self.db.commit()
