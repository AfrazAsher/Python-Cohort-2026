import tkinter as tk

root = tk.Tk()
tk.Label(root, text="I use pack").pack()
tk.Label(root, text="I use grid").grid(row=0, column=0)   # BUG: same parent, two managers
root.mainloop()
