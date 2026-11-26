import tkinter as tk
from tkinter import ttk, messagebox

from library import Library, Book, Magazine, DVD
from library_storage import save_items, load_items

FILENAME = "library.json"
EXTRA_LABELS = {"Book": "Author:", "Magazine": "Issue #:", "DVD": "Runtime (min):"}


class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("City Library")
        self.geometry("700x640")

        self.library = Library("City Library")     # the MODEL: no Tkinter in there
        self.shown = []                            # items currently in the table, in row order
        self.sort_by = None                        # None, "title" or "copies"

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
        self.tree.heading("title", command=lambda: self.sort("title"))     # click a heading to sort
        self.tree.heading("copies", command=lambda: self.sort("copies"))
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

        # --- the add form ---
        form = tk.LabelFrame(self, text="Add an item", padx=10, pady=10)
        form.pack(fill="x", padx=10, pady=5)
        tk.Label(form, text="Type:").grid(row=0, column=0, sticky="e", pady=3)
        self.type_box = ttk.Combobox(form, values=list(EXTRA_LABELS), state="readonly", width=12)
        self.type_box.set("Book")
        self.type_box.grid(row=0, column=1, sticky="w", padx=5, pady=3)
        self.type_box.bind("<<ComboboxSelected>>", lambda event: self.on_type_change())
        tk.Label(form, text="Title:").grid(row=0, column=2, sticky="e", pady=3)
        self.title_entry = tk.Entry(form, width=28)
        self.title_entry.grid(row=0, column=3, padx=5, pady=3)

        self.extra_label = tk.Label(form, text=EXTRA_LABELS["Book"])
        self.extra_label.grid(row=1, column=0, sticky="e", pady=3)
        self.extra_entry = tk.Entry(form, width=16)
        self.extra_entry.grid(row=1, column=1, sticky="w", padx=5, pady=3)
        tk.Label(form, text="Copies:").grid(row=1, column=2, sticky="e", pady=3)
        self.copies_entry = tk.Entry(form, width=6)
        self.copies_entry.insert(0, "1")
        self.copies_entry.grid(row=1, column=3, sticky="w", padx=5, pady=3)
        tk.Button(form, text="Add item", command=self.add_item).grid(row=0, column=4, rowspan=2, padx=10)
        for entry in (self.title_entry, self.extra_entry, self.copies_entry):
            entry.bind("<Return>", lambda event: self.add_item())

        self.status = tk.Label(self, text="", anchor="w")
        self.status.pack(fill="x", padx=10, pady=(0, 10))

        self.load_library()
        self.refresh()

    # ---------- the view ----------
    def visible_items(self):
        keyword = self.search_entry.get().strip().lower()
        items = [item for item in self.library.items if keyword in item.title.lower()]
        if self.sort_by == "title":
            items.sort(key=lambda item: item.title.lower())
        elif self.sort_by == "copies":
            items.sort(key=lambda item: item.get_copies(), reverse=True)
        return items

    def sort(self, column):
        self.sort_by = None if self.sort_by == column else column     # click again = original order
        self.refresh()

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
            self.changed()
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
        self.changed()
        self.select_item(item)
        messagebox.showinfo("Returned", f"Thank you for returning '{item.title}'.")

    def remove(self):
        item = self.selected_item()
        if item is None:
            messagebox.showerror("Oops", "Select an item first.")
            return
        if messagebox.askyesno("Remove", f"Remove '{item.title}' from the library?"):
            self.library.items.remove(item)
            self.changed()

    def on_type_change(self):
        self.extra_label.config(text=EXTRA_LABELS[self.type_box.get()])

    def add_item(self):
        kind = self.type_box.get()
        title = self.title_entry.get().strip()
        extra = self.extra_entry.get().strip()
        if title == "" or extra == "":
            messagebox.showerror("Oops", f"Please fill in the title and {EXTRA_LABELS[kind].rstrip(':').lower()}.")
            return
        try:
            copies = int(self.copies_entry.get())
        except ValueError:
            messagebox.showerror("Oops", "Copies must be a whole number.")
            return
        if copies < 1:
            messagebox.showerror("Oops", "Copies must be at least 1.")
            return

        if kind == "Book":
            item = Book(title, extra, copies)
        elif kind == "Magazine":
            item = Magazine(title, extra, copies)
        else:
            try:
                item = DVD(title, int(extra), copies)
            except ValueError:
                messagebox.showerror("Oops", "Runtime must be a whole number of minutes.")
                return

        if item in self.library.items:                  # uses YOUR __eq__
            messagebox.showerror("Duplicate", f"'{title}' is already in the library.")
            return
        self.library.add_item(item)
        self.changed()
        self.title_entry.delete(0, tk.END)
        self.extra_entry.delete(0, tk.END)
        self.copies_entry.delete(0, tk.END)
        self.copies_entry.insert(0, "1")
        self.title_entry.focus()

    # ---------- saving and loading ----------
    def changed(self):                                  # call after ANY change to the data
        save_items(self.library.items, FILENAME)
        self.refresh()

    def load_library(self):
        items = load_items(FILENAME)
        if items is None:                               # first run: start with some samples
            items = [Book("The Great Gatsby", "F. Scott Fitzgerald", 3),
                     Magazine("National Geographic", "2023-09", 5),
                     DVD("Inception", 148, 2),
                     Book("Dune", "Frank Herbert", 2)]
        for item in items:
            self.library.add_item(item)
        save_items(self.library.items, FILENAME)


if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()
