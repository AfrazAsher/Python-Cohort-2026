import tkinter as tk


class Calculator:
    """A simple four-function calculator."""

    KEYS = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
    ]

    def __init__(self, root):
        root.title("Calculator")
        root.resizable(False, False)

        # --- the calculator's memory (its state) ---
        self.text = "0"          # what the screen shows
        self.first = None        # the number typed before the operator
        self.operator = None     # "+", "-", "*" or "/"
        self.fresh = True        # True = the next digit starts a NEW number

        # --- the screen ---
        self.display = tk.Label(
            root, text=self.text, font=("Arial", 28), width=12,
            anchor="e", bg="white", padx=10, pady=10,
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

        # --- the buttons ---
        for r, row in enumerate(self.KEYS, start=1):
            for c, key in enumerate(row):
                tk.Button(
                    root, text=key, width=5, height=2, font=("Arial", 16),
                    command=lambda k=key: self.press(k),
                ).grid(row=r, column=c, padx=2, pady=2)

        tk.Button(
            root, text="C", height=2, font=("Arial", 16),
            command=lambda: self.press("C"),
        ).grid(row=5, column=0, columnspan=4, sticky="ew", padx=2, pady=2)

    # ---------- the screen ----------
    def show(self, text):
        self.text = text
        self.display.config(text=text)

    # ---------- one button press ----------
    def press(self, key):
        match key:
            case "C":
                self.clear()
            case "=":
                self.equals()
            case "+" | "-" | "*" | "/":
                self.choose_operator(key)
            case ".":
                self.add_dot()
            case _:
                self.add_digit(key)

    def add_digit(self, digit):
        if self.fresh or self.text == "0":
            self.show(digit)                 # start a new number
        else:
            self.show(self.text + digit)     # keep typing the same number
        self.fresh = False

    def add_dot(self):
        if self.fresh:
            self.show("0.")
            self.fresh = False
        elif "." not in self.text:           # only one dot per number
            self.show(self.text + ".")

    def choose_operator(self, op):
        if self.text == "Error":
            return
        if self.operator is not None and not self.fresh:
            self.equals()                    # 2 + 3 + ... finish 2 + 3 first
            if self.text == "Error":
                return
        self.first = float(self.text)
        self.operator = op
        self.fresh = True

    def equals(self):
        if self.operator is None or self.fresh:
            return                           # nothing to calculate yet
        second = float(self.text)
        try:
            result = self.calculate(self.first, self.operator, second)
        except ZeroDivisionError:
            self.show("Error")
            self.reset_state()
            return
        self.show(self.format_number(result))
        self.reset_state()

    def clear(self):
        self.reset_state()
        self.show("0")

    def reset_state(self):
        self.first = None
        self.operator = None
        self.fresh = True

    # ---------- helpers that don't need self ----------
    @staticmethod
    def calculate(a, op, b):
        match op:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                return a / b

    @staticmethod
    def format_number(number):
        if number.is_integer():
            return str(int(number))          # 5.0 -> "5"
        return str(round(number, 10))        # 0.30000000000000004 -> "0.3"


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
