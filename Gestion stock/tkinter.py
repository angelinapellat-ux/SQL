import tkinter as tk
from tkinter import ttk
from gstock import StoreDB  

db = StoreDB()

def refresh_table():
    for row in table.get_children():
        table.delete(row)
    for p in db.get_products():
        table.insert("", "end", values=p)

def add_product():
    db.add_product(
        entry_name.get(),
        entry_desc.get(),
        int(entry_price.get()),
        int(entry_qty.get()),
        int(entry_cat.get())
    )
    refresh_table()

def delete_product():
    selected = table.selection()
    if selected:
        item = table.item(selected)
        product_id = item["values"][0]
        db.delete_product(product_id)
        refresh_table()

def update_product():
    selected = table.selection()
    if selected:
        item = table.item(selected)
        product_id = item["values"][0]
        db.update_product(
            product_id,
            entry_name.get(),
            int(entry_price.get()),
            int(entry_qty.get())
        )
        refresh_table()

