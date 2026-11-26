import tkinter as tk
from tkinter import ttk

from library import Library, Book, Magazine, DVD      # YOUR classes: no Tkinter in there!


class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("City Library")
        self.geometry("700x420")

        # the MODEL: your own classes, doing the real work
        self.library = Library("City Library")
        self.library.add_item(Book("The Great Gatsby", "F. Scott Fitzgerald", 3))
        self.library.add_item(Magazine("National Geographic", "2023-09", 5))
        self.library.add_item(DVD("Inception", 148, 2))
        self.library.add_item(Book("Dune", "Frank Herbert", 2))

        self.shown = []                       # the items currently in the table, in row order

        # the VIEW: a table, a details line, a status line
        columns = ("type", "title", "status", "copies", "loan")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", selectmode="browse")
        for column, heading, width in [("type", "Type", 90), ("title", "Title", 280),
                                       ("status", "Status", 100), ("copies", "Copies", 70),
                                       ("loan", "Loan days", 80)]:
            self.tree.heading(column, text=heading)
            self.tree.column(column, width=width)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", lambda event: self.show_details())

        self.details = tk.Label(self, text="Select an item to see its details",
                                anchor="w", font=("Arial", 11))
        self.details.pack(fill="x", padx=10)
        self.status = tk.Label(self, text="", anchor="w")
        self.status.pack(fill="x", padx=10, pady=10)

        self.refresh()

    def refresh(self):
        self.shown = list(self.library.items)
        self.tree.delete(*self.tree.get_children())
        for index, item in enumerate(self.shown):
            self.tree.insert("", tk.END, iid=str(index), values=(
                type(item).__name__,          # Book / Magazine / DVD
                item.title,
                item.get_status(),
                item.get_copies(),
                item.loan_days(),             # 14 / 7 / 3: each class answers for itself
            ))
        self.status.config(text=f"{len(self.shown)} items")

    def selected_item(self):
        selection = self.tree.selection()
        return self.shown[int(selection[0])] if selection else None

    def show_details(self):
        item = self.selected_item()
        self.details.config(text=str(item) if item else "Select an item to see its details")


if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()
