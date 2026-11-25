import tkinter as tk
from tkinter import messagebox

def add_item():
    text = entry.get().strip()
    if text == "":
        return
    listbox.insert(tk.END, text)             # tk.END = add at the bottom
    entry.delete(0, tk.END)
    entry.focus()

def remove_item():
    selection = listbox.curselection()       # a tuple like (2,) -- empty if nothing is selected
    if not selection:
        messagebox.showerror("Oops", "Select an item first.")
        return
    listbox.delete(selection[0])

def on_select(event):
    selection = listbox.curselection()
    if selection:
        status.config(text="Selected: " + listbox.get(selection[0]))

root = tk.Tk()
root.title("Fruit List")

top = tk.Frame(root)
top.pack(padx=10, pady=10)
entry = tk.Entry(top, width=18)
entry.pack(side="left")
tk.Button(top, text="Add", command=add_item).pack(side="left", padx=5)

middle = tk.Frame(root)
middle.pack(padx=10)
scrollbar = tk.Scrollbar(middle)
scrollbar.pack(side="right", fill="y")
listbox = tk.Listbox(middle, height=6, width=28, yscrollcommand=scrollbar.set)
listbox.pack(side="left")
scrollbar.config(command=listbox.yview)

for fruit in ["Apple", "Banana", "Cherry", "Mango"]:
    listbox.insert(tk.END, fruit)

tk.Button(root, text="Remove selected", command=remove_item).pack(pady=8)
status = tk.Label(root, text="Nothing selected")
status.pack(pady=(0, 10))

listbox.bind("<<ListboxSelect>>", on_select)
entry.bind("<Return>", lambda event: add_item())

root.mainloop()
