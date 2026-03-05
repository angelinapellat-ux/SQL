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

root = tk.Tk()
root.title("Gestion de Stock - Store")

table = ttk.Treeview(root, columns=("ID", "Nom", "Prix", "Quantité", "Catégorie"), show="headings")
for col in ("ID", "Nom", "Prix", "Quantité", "Catégorie"):
    table.heading(col, text=col)
table.pack()

tk.Label(root, text="Nom").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Description").pack()
entry_desc = tk.Entry(root)
entry_desc.pack()

tk.Label(root, text="Prix").pack()
entry_price = tk.Entry(root)
entry_price.pack()

tk.Label(root, text="Quantité").pack()
entry_qty = tk.Entry(root)
entry_qty.pack()

tk.Label(root, text="ID Catégorie").pack()
entry_cat = tk.Entry(root)
entry_cat.pack()

tk.Button(root, text="Ajouter", command=add_product).pack()
tk.Button(root, text="Modifier", command=update_product).pack()
tk.Button(root, text="Supprimer", command=delete_product).pack()

refresh_table()
root.mainloop()
