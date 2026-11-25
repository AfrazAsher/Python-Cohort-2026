import tkinter as tk
from tkinter import messagebox


class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("360x420")

        top = tk.Frame(self)
        top.pack(fill="x", padx=10, pady=10)
        self.entry = tk.Entry(top, font=("Arial", 12))
        self.entry.pack(side="left", fill="x", expand=True)
        tk.Button(top, text="Add", command=self.add_task).pack(side="left", padx=(5, 0))

        middle = tk.Frame(self)
        middle.pack(fill="both", expand=True, padx=10)
        scrollbar = tk.Scrollbar(middle)
        scrollbar.pack(side="right", fill="y")
        self.listbox = tk.Listbox(middle, font=("Arial", 12), yscrollcommand=scrollbar.set)
        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.listbox.yview)

        tk.Button(self, text="Delete selected", command=self.delete_task).pack(pady=10)

        self.entry.bind("<Return>", lambda event: self.add_task())
        self.entry.focus()

    def add_task(self):
        text = self.entry.get().strip()
        if text == "":
            return
        self.listbox.insert(tk.END, text)
        self.entry.delete(0, tk.END)

    def delete_task(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showerror("Oops", "Select a task first.")
            return
        self.listbox.delete(selection[0])


if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
