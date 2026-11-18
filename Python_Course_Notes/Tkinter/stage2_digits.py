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
        root.resizable(False, False)

        self.text = "0"                       # what the screen shows

        self.display = tk.Label(root, text=self.text, font=("Arial", 28), width=12,
                                anchor="e", bg="white", padx=10, pady=10)
        self.display.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

        for r, row in enumerate(self.KEYS, start=1):
            for c, key in enumerate(row):
                tk.Button(root, text=key, width=5, height=2, font=("Arial", 16),
                          command=lambda k=key: self.press(k)
                          ).grid(row=r, column=c, padx=2, pady=2)

        tk.Button(root, text="C", height=2, font=("Arial", 16),
                  command=lambda: self.press("C")
                  ).grid(row=5, column=0, columnspan=4, sticky="ew", padx=2, pady=2)

    def show(self, text):
        self.text = text
        self.display.config(text=text)

    def press(self, key):
        if key == "C":
            self.show("0")
        elif key == ".":
            if "." not in self.text:          # only one dot per number
                self.show(self.text + ".")
        elif key in "+-*/=":
            print("operator pressed:", key)   # not wired up yet!
        else:                                 # a digit
            if self.text == "0":
                self.show(key)                # replace the lonely 0
            else:
                self.show(self.text + key)


root = tk.Tk()
Calculator(root)
root.mainloop()
