import random
import tkinter as tk

quotes = [
    "Practice makes progress.",
    "Every expert was once a beginner.",
    "Bugs are just lessons in disguise.",
    "Read the error message. Really.",
]
colors = ["darkgreen", "navy", "purple", "darkred", "teal"]

def new_quote():
    quote_label.config(text=random.choice(quotes), bg=random.choice(colors))

root = tk.Tk()
root.title("Quote Machine")
root.geometry("420x220")

quote_label = tk.Label(
    root, text="Press the button!", font=("Arial", 16),
    fg="white", bg="gray", width=32, height=3, wraplength=380,
)
quote_label.pack(pady=20)

tk.Button(root, text="New quote", command=new_quote).pack()

root.mainloop()
