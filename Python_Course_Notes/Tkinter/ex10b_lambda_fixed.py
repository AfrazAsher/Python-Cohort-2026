import tkinter as tk

def show(number):
    label.config(text=f"You pressed {number}")

root = tk.Tk()
root.title("Lambda fixed")

label = tk.Label(root, text="Press a button", font=("Arial", 14))
label.pack(pady=10)

for n in [1, 2, 3]:
    tk.Button(root, text=n, width=6,
              command=lambda n=n: show(n)).pack(side="left", padx=5, pady=10)

root.mainloop()
