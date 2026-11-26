class LibraryItem:
    total_items = 0
    VALID_STATUSES = ["Available", "Borrowed", "Lost", "Under Repair"]

    def __init__(self, title, copies=1):
        self.title = title
        self._status = "Available"
        self._copies = 0
        self.set_copies(copies)
        LibraryItem.total_items += 1

    def get_status(self):
        return self._status

    def get_copies(self):
        return self._copies

    def set_status(self, new_status):
        if new_status in LibraryItem.VALID_STATUSES:
            self._status = new_status
            return True
        print(
            f"Invalid status '{new_status}'. "
            f"Choose from: {LibraryItem.VALID_STATUSES}"
        )
        return False

    def set_copies(self, new_copies):
        if new_copies >= 0:
            self._copies = new_copies
            return True
        print("Copies cannot be negative.")
        return False

    def loan_days(self):
        return 14

    def borrow(self):
        if self._status == "Available" and self._copies > 0:
            self.set_copies(self._copies - 1)

            if self._copies == 0:
                self.set_status("Borrowed")

            print(f"You borrowed '{self.title}'.")
            print(f"Please return it within {self.loan_days()} days.")
            return True

        print(f"Sorry, '{self.title}' is not available right now.")
        return False

    def return_item(self):
        self.set_copies(self._copies + 1)
        self.set_status("Available")
        print(f"Thank you for returning '{self.title}'.")

    def __str__(self):
        return f"{self.title} [{self._status}, {self._copies} left]"

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f"(title={self.title!r}, copies={self._copies})"
        )

    def __eq__(self, other):
        if not isinstance(other, LibraryItem):
            return False

        same_type = type(self) == type(other)
        return same_type and self.title.lower() == other.title.lower()


class Book(LibraryItem):
    def __init__(self, title, author, copies=1):
        super().__init__(title, copies)
        self.author = author

    def __str__(self):
        return f"(Book) {super().__str__()} by {self.author}"


class Magazine(LibraryItem):
    def __init__(self, title, issue_number, copies=1):
        super().__init__(title, copies)
        self.issue_number = issue_number

    def loan_days(self):
        return 7

    def __str__(self):
        return f"(Magazine) {super().__str__()} (Issue #{self.issue_number})"


class DVD(LibraryItem):
    def __init__(self, title, runtime_minutes, copies=1):
        super().__init__(title, copies)
        self.runtime_minutes = runtime_minutes

    def loan_days(self):
        return 3

    def __str__(self):
        return (
            f"(DVD) {super().__str__()} "
            f"({self.runtime_minutes} min)"
        )


class Library:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        if not isinstance(item, LibraryItem):
            print("Only library items can be added.")
            return

        if item in self.items:
            print(f"'{item.title}' is already in the library.")
            return

        self.items.append(item)
        print(f"Added: {item}")

    def view_all(self):
        print(f"\n--- {self.name}: All Items ---")
        for item in self.items:
            print(item)

    def view_sorted(self, by="title"):
        if by == "title":
            ordered = sorted(
                self.items,
                key=lambda i: i.title.lower()
            )
            heading = "A to Z"
        else:
            ordered = sorted(
                self.items,
                key=lambda i: i.get_copies(),
                reverse=True
            )
            heading = "Most Copies First"

        print(f"\n--- {self.name}: {heading} ---")
        for item in ordered:
            print(item)

    def search(self, keyword):
        found = False

        for item in self.items:
            if keyword.lower() in item.title.lower():
                print(item)
                found = True

        if not found:
            print("No matching items found.")

    def find_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                return item
        return None

    def borrow_item(self, title):
        item = self.find_item(title)

        if item is None:
            print("Item not found.")
        else:
            item.borrow()

    def return_item(self, title):
        item = self.find_item(title)

        if item is None:
            print("Item not found.")
        else:
            item.return_item()


if __name__ == "__main__":
    Library = Library("City Library")
    Library.add_item(Book("The Great Gatsby", "F. Scott Fitzgerald", 3))
    Library.add_item(Magazine("National Geographic", "2023-09", 5))
    Library.add_item(DVD("Inception", 148, 2))
    Library.view_all()