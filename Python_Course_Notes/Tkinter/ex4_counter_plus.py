import tkinter as tk

count = 0

def on_click():
    global count
    count += 1
    label.config(text=f"Clicked {count} times")

def reset():
    global count
    count = 0
    label.config(text="Clicked 0 times")

root = tk.Tk()
root.title("Click Counter")
root.geometry("320x240")
root.config(bg="lightblue")          # the window itself can be coloured too

label = tk.Label(root, text="Clicked 0 times", font=("Arial", 16), bg="lightblue")
label.pack(pady=20)

tk.Button(root, text="Click me!", command=on_click).pack(pady=5)
tk.Button(root, text="Reset", command=reset).pack(pady=5)
tk.Button(root, text="Quit", command=root.destroy).pack(pady=5)   # root.destroy: no ()!

root.mainloop()
