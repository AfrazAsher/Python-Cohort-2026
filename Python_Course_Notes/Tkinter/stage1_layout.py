import tkinter as tk


class Calculator:
    KEYS = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
    ]

    def __init__(self, root):
        root.title("Calculator")

        self.display = tk.Label(root, text="0", font=("Arial", 28), width=12, anchor="e", bg="white")
        self.display.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

        for r, row in enumerate(self.KEYS, start=1):
            for c, key in enumerate(row):
                tk.Button(
                    root, text=key, width=5, height=2, font=("Arial", 16),
                    command=lambda k=key: self.press(k),
                ).grid(row=r, column=c, padx=2, pady=2)

    def press(self, key):
        print("You pressed", key)
        self.display.config(text=key)


root = tk.Tk()
Calculator(root)
root.mainloop()
