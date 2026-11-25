import tkinter as tk

root = tk.Tk()
root.title("Profile Form")

# Each Frame is its own little container, so each can choose its OWN layout manager.
form = tk.LabelFrame(root, text="Details", padx=10, pady=10)
form.pack(padx=10, pady=10)                 # root uses pack for its frames...

tk.Label(form, text="Name:").grid(row=0, column=0, sticky="e", pady=3)   # ...the form uses grid inside
name_entry = tk.Entry(form, width=20)
name_entry.grid(row=0, column=1, pady=3)
tk.Label(form, text="Email:").grid(row=1, column=0, sticky="e", pady=3)
email_entry = tk.Entry(form, width=20)
email_entry.grid(row=1, column=1, pady=3)

buttons = tk.Frame(root)
buttons.pack(pady=5)
tk.Button(buttons, text="Save").pack(side="left", padx=5)     # side="left": a row of buttons
tk.Button(buttons, text="Cancel").pack(side="left", padx=5)

root.mainloop()
