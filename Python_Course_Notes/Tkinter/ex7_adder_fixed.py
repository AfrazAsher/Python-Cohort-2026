import tkinter as tk
from tkinter import messagebox

def add():
    try:
        total = float(first.get()) + float(second.get())   # text -> number first
    except ValueError:
        messagebox.showerror("Oops", "Please type two numbers.")
        return
    result.config(text=f"Total: {total:g}")

root = tk.Tk()
root.title("Adder")

first = tk.Entry(root, width=10, font=("Arial", 14))
first.grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="+", font=("Arial", 14)).grid(row=0, column=1)
second = tk.Entry(root, width=10, font=("Arial", 14))
second.grid(row=0, column=2, padx=10, pady=10)

tk.Button(root, text="Add", command=add).grid(row=1, column=0, columnspan=3, pady=5)
result = tk.Label(root, text="", font=("Arial", 16))
result.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
