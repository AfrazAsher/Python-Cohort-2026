import tkinter as tk

count = 0

def on_click():
    global count
    count += 1
    label.config(text=f"Clicked {count} times")

root = tk.Tk()
root.title("Click Counter")
root.geometry("320x200")

label = tk.Label(root, text="Clicked 0 times", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="Click me!", command=on_click)   # no () after on_click!
button.pack()

root.mainloop()
