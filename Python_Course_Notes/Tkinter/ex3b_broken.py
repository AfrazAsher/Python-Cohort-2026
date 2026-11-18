import tkinter as tk

count = 0

def on_click():
    global count
    count += 1
    print("on_click was called, count is", count)
    label.config(text=f"Clicked {count} times")

root = tk.Tk()
root.title("Broken Counter")
root.geometry("320x200")

label = tk.Label(root, text="Clicked 0 times", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="Click me!", command=on_click())   # BUG: () runs it right away
button.pack()

root.mainloop()
