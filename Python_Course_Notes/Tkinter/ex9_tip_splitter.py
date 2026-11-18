import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        bill = float(bill_entry.get())
        tip = float(tip_entry.get())
        people = int(people_entry.get())
    except ValueError:
        messagebox.showerror("Oops", "Please enter numbers in all three boxes.")
        return
    if people <= 0:
        messagebox.showerror("Oops", "There must be at least 1 person.")
        return
    total = bill * (1 + tip / 100)
    result.config(text=f"Total: {total:.2f}    Each: {total / people:.2f}")

root = tk.Tk()
root.title("Tip Splitter")

tk.Label(root, text="Bill:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
bill_entry = tk.Entry(root, width=10)
bill_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Tip %:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tip_entry = tk.Entry(root, width=10)
tip_entry.insert(0, "10")                 # a sensible default
tip_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="People:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
people_entry = tk.Entry(root, width=10)
people_entry.insert(0, "1")
people_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=8)
result = tk.Label(root, text="", font=("Arial", 12))
result.grid(row=4, column=0, columnspan=2, pady=8)

root.mainloop()
