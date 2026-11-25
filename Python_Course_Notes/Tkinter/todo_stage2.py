import tkinter as tk
from tkinter import messagebox


class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("360x440")

        self.tasks = []                    # the DATA: a list of [text, done] pairs

        top = tk.Frame(self)
        top.pack(fill="x", padx=10, pady=10)
        self.entry = tk.Entry(top, font=("Arial", 12))
        self.entry.pack(side="left", fill="x", expand=True)
        tk.Button(top, text="Add", command=self.add_task).pack(side="left", padx=(5, 0))

        middle = tk.Frame(self)
        middle.pack(fill="both", expand=True, padx=10)
        scrollbar = tk.Scrollbar(middle)
        scrollbar.pack(side="right", fill="y")
        self.listbox = tk.Listbox(middle, font=("Arial", 12), activestyle="none",
                                  yscrollcommand=scrollbar.set)
        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.listbox.yview)

        buttons = tk.Frame(self)
        buttons.pack(pady=10)
        tk.Button(buttons, text="Done / Undo", command=self.toggle_done).pack(side="left", padx=5)
        tk.Button(buttons, text="Delete", command=self.delete_task).pack(side="left", padx=5)

        self.status = tk.Label(self, text="", anchor="w")
        self.status.pack(fill="x", padx=10, pady=(0, 10))

        self.entry.bind("<Return>", lambda event: self.add_task())
        self.listbox.bind("<Double-Button-1>", lambda event: self.toggle_done())
        self.entry.focus()
        self.refresh()

    # ---- the listbox is only a VIEW of self.tasks: redraw it from the data ----
    def refresh(self):
        self.listbox.delete(0, tk.END)
        for text, done in self.tasks:
            prefix = "[x] " if done else "[ ] "
            self.listbox.insert(tk.END, prefix + text)
            if done:
                self.listbox.itemconfig(tk.END, fg="gray")
        finished = sum(1 for _, done in self.tasks if done)
        self.status.config(text=f"{finished} of {len(self.tasks)} done")

    def selected_index(self):
        selection = self.listbox.curselection()
        return selection[0] if selection else None

    def add_task(self):
        text = self.entry.get().strip()
        if text == "":
            return
        self.tasks.append([text, False])
        self.entry.delete(0, tk.END)
        self.refresh()

    def toggle_done(self):
        index = self.selected_index()
        if index is None:
            messagebox.showerror("Oops", "Select a task first.")
            return
        self.tasks[index][1] = not self.tasks[index][1]
        self.refresh()
        self.listbox.selection_set(index)      # keep the same row selected

    def delete_task(self):
        index = self.selected_index()
        if index is None:
            messagebox.showerror("Oops", "Select a task first.")
            return
        del self.tasks[index]
        self.refresh()


if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
