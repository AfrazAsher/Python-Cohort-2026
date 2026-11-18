import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        celsius = float(entry.get())
    except ValueError:
        messagebox.showerror("Oops", "Please enter a number.")
        return
    fahrenheit = celsius * 9 / 5 + 32
    result.config(text=f"{celsius:g} °C = {fahrenheit:g} °F")

def clear():
    entry.delete(0, tk.END)       # remove everything from position 0 to the end
    result.config(text="")
    entry.focus()                 # put the cursor back in the box

root = tk.Tk()
root.title("Temperature Converter")

tk.Label(root, text="Celsius:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry = tk.Entry(root, width=12, font=("Arial", 12))
entry.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Convert", command=convert).grid(row=1, column=0, padx=10, pady=5)
tk.Button(root, text="Clear", command=clear).grid(row=1, column=1, padx=10, pady=5)

result = tk.Label(root, text="", font=("Arial", 14))
result.grid(row=2, column=0, columnspan=2, pady=10)

root.bind("<Return>", lambda event: convert())     # pressing Enter also converts

root.mainloop()
