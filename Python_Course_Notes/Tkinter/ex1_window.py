import tkinter as tk

root = tk.Tk()                    # create the main window
root.title("My First Window")     # text in the title bar
root.geometry("420x300")          # width x height in pixels

root.mainloop()                   # show the window and WAIT for the user
print("Window closed!")           # runs only AFTER the window is closed
