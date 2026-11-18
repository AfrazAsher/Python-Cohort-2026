import tkinter as tk

root = tk.Tk()
root.title("Hello")
root.geometry("320x200")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 18), fg="white", bg="darkgreen")
label.pack(pady=30)               # place it in the window

root.mainloop()
