import tkinter as tk
from tkinter import ttk, messagebox

from library import Library, Book, Magazine, DVD


class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("City Library")
        self.geometry("700x480")

        self.library = Library("City Library")
        self.library.add_item(Book("The Great Gatsby", "F. Scott Fitzgerald", 3))
        self.library.add_item(Magazine("National Geographic", "2023-09", 5))
        self.library.add_item(DVD("Inception", 148, 2))
        self.library.add_item(Book("Dune", "Frank Herbert", 2))

        self.shown = []

        # --- search bar ---
        top = tk.Frame(self)
        top.pack(fill="x", padx=10, pady=(10, 5))
        tk.Label(top, text="Search:").pack(side="left")
        self.search_entry = tk.Entry(top, font=("Arial", 11))
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5)
        self.search_entry.bind("<KeyRelease>", lambda event: self.refresh())

        # --- table ---
        columns = ("type", "title", "status", "copies", "loan")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", selectmode="browse")
        for column, heading, width in [("type", "Type", 90), ("title", "Title", 280),
                                       ("status", "Status", 100), ("copies", "Copies", 70),
                                       ("loan", "Loan days", 80)]:
            self.tree.heading(column, text=heading)
            self.tree.column(column, width=width)
        self.tree.tag_configure("unavailable", foreground="gray")
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)
        self.tree.bind("<<TreeviewSelect>>", lambda event: self.show_details())

        self.details = tk.Label(self, text="", anchor="w", font=("Arial", 11))
        self.details.pack(fill="x", padx=10)

        # --- buttons ---
        buttons = tk.Frame(self)
        buttons.pack(pady=8)
        tk.Button(buttons, text="Borrow", width=10, command=self.borrow).pack(side="left", padx=5)
        tk.Button(buttons, text="Return", width=10, command=self.give_back).pack(side="left", padx=5)
        tk.Button(buttons, text="Remove", width=10, command=self.remove).pack(side="left", padx=5)

        self.status = tk.Label(self, text="", anchor="w")
        self.status.pack(fill="x", padx=10, pady=(0, 10))

        self.refresh()

    # ---------- the view ----------
    def visible_items(self):
        keyword = self.search_entry.get().strip().lower()
        return [item for item in self.library.items if keyword in item.title.lower()]

    def refresh(self):
        self.shown = self.visible_items()
        self.tree.delete(*self.tree.get_children())
        for index, item in enumerate(self.shown):
            tags = () if item.get_status() == "Available" else ("unavailable",)
            self.tree.insert("", tk.END, iid=str(index), tags=tags, values=(
                type(item).__name__, item.title, item.get_status(),
                item.get_copies(), item.loan_days(),
            ))
        self.status.config(text=f"Showing {len(self.shown)} of {len(self.library.items)} items")
        self.show_details()

    def selected_item(self):
        selection = self.tree.selection()
        return self.shown[int(selection[0])] if selection else None

    def select_item(self, item):
        for index, shown_item in enumerate(self.shown):
            if shown_item is item:
                self.tree.selection_set(str(index))

    def show_details(self):
        item = self.selected_item()
        self.details.config(text=str(item) if item else "Select an item to see its details")

    # ---------- the buttons ----------
    def borrow(self):
        item = self.selected_item()
        if item is None:
            messagebox.showerror("Oops", "Select an item first.")
            return
        if item.borrow():                              # your method returns True / False
            self.refresh()
            self.select_item(item)
            messagebox.showinfo("Borrowed", f"Enjoy '{item.title}'!\n"
                                            f"Please return it within {item.loan_days()} days.")
        else:
            messagebox.showerror("Not available", f"Sorry, '{item.title}' is not available right now.")

    def give_back(self):
        item = self.selected_item()
        if item is None:
            messagebox.showerror("Oops", "Select an item first.")
            return
        item.return_item()
        self.refresh()
        self.select_item(item)
        messagebox.showinfo("Returned", f"Thank you for returning '{item.title}'.")

    def remove(self):
        item = self.selected_item()
        if item is None:
            messagebox.showerror("Oops", "Select an item first.")
            return
        if messagebox.askyesno("Remove", f"Remove '{item.title}' from the library?"):
            self.library.items.remove(item)
            self.refresh()


if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()
