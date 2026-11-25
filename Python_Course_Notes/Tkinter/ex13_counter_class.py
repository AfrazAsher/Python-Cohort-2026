import tkinter as tk


class CounterApp(tk.Tk):                      # our app IS a window
    def __init__(self):
        super().__init__()                    # build the real Tk window first
        self.title("Click Counter")
        self.geometry("320x240")

        self.count = 0                        # memory lives on the object: no global!

        self.label = tk.Label(self, text="Clicked 0 times", font=("Arial", 16))
        self.label.pack(pady=20)
        tk.Button(self, text="Click me!", command=self.on_click).pack(pady=5)
        tk.Button(self, text="Reset", command=self.reset).pack(pady=5)
        tk.Button(self, text="Quit", command=self.destroy).pack(pady=5)

    def on_click(self):
        self.count += 1
        self.label.config(text=f"Clicked {self.count} times")

    def reset(self):
        self.count = 0
        self.label.config(text="Clicked 0 times")


if __name__ == "__main__":
    app = CounterApp()
    app.mainloop()
