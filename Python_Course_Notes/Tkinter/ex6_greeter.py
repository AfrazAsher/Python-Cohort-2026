import tkinter as tk

def greet():
    name = entry.get().strip()
    if name == "":
        result.config(text="Please type your name first!")
    else:
        result.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("Greeter")
root.geometry("320x220")

tk.Label(root, text="What is your name?", font=("Arial", 14)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

tk.Button(root, text="Greet me", command=greet).pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 16))
result.pack()

root.mainloop()
