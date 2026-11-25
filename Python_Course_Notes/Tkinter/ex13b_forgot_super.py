import tkinter as tk


class CounterApp(tk.Tk):
    def __init__(self):
        # BUG: forgot super().__init__()
        self.title("Click Counter")


app = CounterApp()
app.mainloop()
