import tkinter as tk
from tkinter import ttk

people = [("Ali", 15, "Lahore"), ("Sara", 16, "Karachi"), ("Omar", 21, "Islamabad")]

def show_selected():
    selection = tree.selection()               # a tuple of row ids: empty if nothing is selected
    if not selection:
        status.config(text="Nothing selected")
        return
    name, age, city = tree.item(selection[0], "values")
    status.config(text=f"{name} is {age} and lives in {city}")

def delete_selected():
    for row_id in tree.selection():
        tree.delete(row_id)

root = tk.Tk()
root.title("Treeview demo")

tree = ttk.Treeview(root, columns=("name", "age", "city"), show="headings", height=6)
for column, heading, width in [("name", "Name", 120), ("age", "Age", 60), ("city", "City", 120)]:
    tree.heading(column, text=heading)
    tree.column(column, width=width)

for person in people:
    tree.insert("", tk.END, values=person)       # one row per tuple
tree.pack(padx=10, pady=10)

buttons = tk.Frame(root)
buttons.pack()
tk.Button(buttons, text="Show selected", command=show_selected).pack(side="left", padx=5)
tk.Button(buttons, text="Delete selected", command=delete_selected).pack(side="left", padx=5)

status = tk.Label(root, text="Click a row")
status.pack(pady=10)

root.mainloop()
