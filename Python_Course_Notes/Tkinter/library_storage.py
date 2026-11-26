"""Saving and loading a Library as JSON.  No Tkinter in here either."""
import json
import os

from library import Book, Magazine, DVD

# class to rebuild, and the name of its "extra" attribute
TYPES = {
    "Book": (Book, "author"),
    "Magazine": (Magazine, "issue_number"),
    "DVD": (DVD, "runtime_minutes"),
}


def item_to_dict(item):
    name = type(item).__name__
    _, extra_attribute = TYPES[name]
    return {
        "type": name,
        "title": item.title,
        "extra": getattr(item, extra_attribute),
        "copies": item.get_copies(),
        "status": item.get_status(),
    }


def dict_to_item(data):
    cls, _ = TYPES[data["type"]]
    item = cls(data["title"], data["extra"], data["copies"])
    item.set_status(data["status"])
    return item


def save_items(items, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump([item_to_dict(item) for item in items], file, indent=4)


def load_items(filename):
    """Return a list of items, or None if there is no usable file."""
    try:
        with open(filename, encoding="utf-8") as file:
            return [dict_to_item(data) for data in json.load(file)]
    except FileNotFoundError:
        return None                                   # first run
    except (json.JSONDecodeError, KeyError, TypeError):
        os.replace(filename, filename + ".bad")       # keep the broken file, don't destroy it
        print(f"{filename} could not be read. Saved a copy as {filename}.bad")
        return None
