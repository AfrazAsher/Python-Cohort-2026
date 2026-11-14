# 00 · Developer Tools Guide
### Git & GitHub · Running Python files · Modules · `pip` · Virtual environments

This guide covers the tools that live **outside** your notebooks. They need a **terminal** (a window where you type commands), so they are not written as notebook cells. Keep this page open next to your terminal.

> **Where is my terminal?**
> - **Windows:** open *PowerShell* or *Windows Terminal* (or use the terminal inside VS Code: `` Ctrl + ` ``)
> - **Mac / Linux:** open *Terminal*
>
> Commands start after the `$` in the examples below. **Don't type the `$`.**

**Contents**
1. [Git and GitHub](#1-git-and-github)
2. [Running a Python file from the terminal](#2-running-a-python-file)
3. [Modules: your own files and `__name__`](#3-modules-your-own-files-and-__name__)
4. [`pip`: installing other people's code](#4-pip-installing-other-peoples-code)
5. [Virtual environments and `requirements.txt`](#5-virtual-environments-and-requirementstxt)
6. [`.gitignore`: what NOT to upload](#6-gitignore-what-not-to-upload)
7. [Cheat sheet](#7-cheat-sheet)
8. [Troubleshooting](#8-troubleshooting)

---

## 1. Git and GitHub

### The problem
Has this ever happened to you?

```text
project_final.py
project_final_v2.py
project_final_v2_REALLY_FINAL.py
project_final_v2_REALLY_FINAL_fixed.py
```

**Git** solves this. It tracks every change you make to your code over time, so you never need a second copy "just in case".

| | What it is |
|---|---|
| **Git** | the tool on **your computer** that tracks changes (works offline) |
| **GitHub** | a **website** that stores your Git projects online, so you can share them and show them to others |

> Git is the engine; GitHub is one of many places to park the car. You could use Git forever without GitHub, but GitHub is where your code becomes your **portfolio**.

💡 *Fun facts:* Git was created in 2005 by Linus Torvalds (the creator of Linux) in about ten days. GitHub hosts well over 100 million repositories, including Python itself.

### Vocabulary

| Term | Plain-English meaning |
|---|---|
| **Repository (repo)** | a project folder that Git is tracking |
| **Commit** | a saved **snapshot** of your code, with a message saying what changed |
| **Stage** (`git add`) | choosing which changes go into the next snapshot |
| **Push** | upload your commits to GitHub |
| **Pull** | download new changes from GitHub |
| **Clone** | copy an existing GitHub repo onto your computer |

### Check that Git is installed
```bash
$ git --version
```
(Same idea as `sys.version` for Python.) If it isn't installed, download it from <https://git-scm.com>.

### One-time setup (tells Git who you are)
```bash
$ git config --global user.name "Your Name"
$ git config --global user.email "you@example.com"
```

### Your first repository
```bash
$ mkdir first-project
$ cd first-project
$ git init
$ echo "# My First Project" > README.md
$ git add README.md
$ git commit -m "Initial commit"
```

- `git add` = *"include this file in the next snapshot"*
- `git commit` = *"take the snapshot"*, with a message explaining what you did

### Connect it to GitHub and push
1. On <https://github.com>, create a **new, empty** repository (no README) and copy its URL.
2. Then:
```bash
$ git remote add origin https://github.com/YOUR-USERNAME/first-project.git
$ git branch -M main
$ git push -u origin main
```
Refresh the GitHub page: your README is there. 🎉

### The everyday routine
After the first setup, your daily Git life is just these three commands:

```bash
$ git add .                       # stage everything that changed
$ git commit -m "Add login check" # snapshot with a clear message
$ git push                        # upload to GitHub
```

Useful extras:

| Command | What it does |
|---|---|
| `git status` | what changed? what is staged? |
| `git log --oneline` | the history of commits |
| `git pull` | download changes from GitHub |
| `git clone <url>` | copy a repo to your computer |

### Writing good commit messages
- ✅ `Add input validation to the guessing game`
- ✅ `Fix crash when the library file is missing`
- ❌ `stuff`, `asdf`, `final final`

---

## 2. Running a Python file

Notebooks are great for learning. Real programs are usually **`.py` files**.

```bash
$ python my_program.py
```
(On some Mac/Linux systems the command is `python3`.)

Check your Python version:
```bash
$ python --version
```

If your program uses `input()`, it asks you in the terminal, exactly like in the notebook.

---

## 3. Modules: your own files and `__name__`

A **module** is any `.py` file. You can `import` it from another file in the **same folder**. This is how we split the Library project:

```text
library_project/
├── library.py     ← the classes (LibraryItem, Book, Magazine, DVD, Library)
└── main.py        ← the menu that uses them
```

**In `main.py`:**
```python
from library import Library, Book, Magazine, DVD

library = Library("City Library")
library.add_item(Book("Dune", "Frank Herbert", 2))
```

Three import styles:

```python
import library                      # library.Book(...)
from library import Book, DVD       # Book(...)
import library as lib               # lib.Book(...)
```

### `if __name__ == "__main__":`
Every file has a hidden variable `__name__`:

| How the file is used | `__name__` is |
|---|---|
| run directly (`python library.py`) | `"__main__"` |
| imported (`import library`) | `"library"` (the file name) |

So at the bottom of `library.py` you can put quick tests that run **only when you run that file directly**, and not when `main.py` imports it:

```python
if __name__ == "__main__":
    shelf = Library("Test Library")
    shelf.add_item(Book("The Great Gatsby", "F. Scott Fitzgerald", 3))
    shelf.view_all()
```

⚠️ **Common problems**
- The imported file must be in the **same folder** (or Python can't find it).
- Never name your file `random.py`, `math.py`, etc. Python would import *yours* instead of the real one.
- Circular imports (`a.py` imports `b.py` and `b.py` imports `a.py`) cause errors. Keep imports going **one direction**.

(There is a runnable demonstration in notebook 07, section 11.)

---

## 4. `pip`: installing other people's code

Python comes with a **standard library** (`random`, `math`, `json`, `os`, …). But millions of other packages exist (`requests`, `flask`, `pandas`, `numpy`, …). **`pip`** is Python's tool for downloading and installing them from **PyPI**, the Python Package Index (almost a million projects).

Always run pip through Python, so it's sure to match the right Python:

```bash
$ python -m pip --version                 # check it works
$ python -m pip install requests          # install a package
$ python -m pip list                      # what is installed?
$ python -m pip show requests             # details about one package
$ python -m pip install requests==2.32.3  # a specific version
$ python -m pip install --upgrade requests
$ python -m pip uninstall requests
```

Test it:
```python
import requests
print(requests.__version__)
```

**In a Jupyter notebook**, use the `%pip` magic so it installs into the notebook's own Python:
```python
%pip install requests
```

> ⚠️ If you ever see `ModuleNotFoundError: No module named 'requests'`, it means the package isn't installed **in the Python you're running**. Install it, then restart the notebook kernel.

---

## 5. Virtual environments and `requirements.txt`

### The problem
Imagine two projects:
- Project A needs `requests` version 2.20
- Project B needs `requests` version 2.32

If everything is installed in one shared place, they fight each other. Also, your computer's Python gets cluttered with packages from every experiment.

### The solution: one clean room per project
A **virtual environment** ("venv") is a private folder containing its own Python and its own installed packages, for **one project**.

### Step by step
Run these **inside your project folder**.

**1. Create it** (do this once per project):
```bash
$ python -m venv venv
```
This makes a folder called `venv`.

**2. Activate it** (do this every time you open a new terminal):

| System | Command |
|---|---|
| **Windows (PowerShell)** | `venv\Scripts\Activate.ps1` |
| **Windows (Command Prompt)** | `venv\Scripts\activate.bat` |
| **Mac / Linux** | `source venv/bin/activate` |

When it works, your prompt starts with `(venv)`:
```text
(venv) C:\Users\You\my-project>
```

> 🪟 **Windows PowerShell error "running scripts is disabled"?** Run this once, then try again:
> `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

**3. Install packages** (they go into `venv` only):
```bash
(venv) $ python -m pip install requests
```

**4. Save the list of packages** so anyone can rebuild your setup:
```bash
(venv) $ python -m pip freeze > requirements.txt
```

**5. Recreate the environment** on another computer (or after deleting `venv`):
```bash
$ python -m venv venv
$ source venv/bin/activate        # (or the Windows version)
(venv) $ python -m pip install -r requirements.txt
```

**6. Leave the environment:**
```bash
(venv) $ deactivate
```

### Golden rules
1. ✅ **Commit `requirements.txt`** to Git.
2. ❌ **Never commit the `venv/` folder.** It is big, specific to your computer, and rebuildable from `requirements.txt`.
3. One virtual environment per project.

---

## 6. `.gitignore`: what NOT to upload

A file named `.gitignore` (note the dot) tells Git which files to **skip**. Put it in the root of your project:

```text
venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
pokedex_cache.json
.env
```

| Entry | Why |
|---|---|
| `venv/` | rebuildable from `requirements.txt` |
| `__pycache__/` | Python's automatic cache files |
| `.ipynb_checkpoints/` | Jupyter's autosave copies |
| `pokedex_cache.json` | data your program creates, not source code |
| `.env` | where **secret keys and passwords** live. Never upload secrets! |

Create `.gitignore` **before** your first `git add .`.

---

## 7. Cheat sheet

| I want to… | Command |
|---|---|
| Check Git / Python | `git --version` · `python --version` |
| Start tracking a folder | `git init` |
| Snapshot my work | `git add .` → `git commit -m "message"` |
| Upload to GitHub | `git push` |
| Run a program | `python file.py` |
| Install a package | `python -m pip install name` |
| Create / activate a venv | `python -m venv venv` · `source venv/bin/activate` (Win: `venv\Scripts\Activate.ps1`) |
| Save / restore packages | `python -m pip freeze > requirements.txt` · `python -m pip install -r requirements.txt` |
| Leave the venv | `deactivate` |

**Recommended project folder**
```text
my-project/
├── .gitignore
├── README.md
├── requirements.txt
├── library.py
├── main.py
└── venv/            ← (ignored by Git)
```

---

## 8. Troubleshooting

| Problem | Likely fix |
|---|---|
| `'python' is not recognized` / `command not found` | Python isn't on your PATH. On Mac/Linux try `python3`. On Windows try `py`. |
| `ModuleNotFoundError: No module named 'x'` | Install it with `python -m pip install x` in the **same** Python/venv you run. Restart the notebook kernel. |
| Installed a package but the notebook can't see it | The notebook uses a different Python. Use `%pip install x` inside the notebook, then restart the kernel. |
| `(venv)` doesn't appear | You forgot to activate the environment. |
| `pip` installs to the wrong place | Always use `python -m pip`, and check for `(venv)` first. |
| `git push` is rejected | Run `git pull` first, then push again. |
| I committed `venv/` by mistake | Add it to `.gitignore`, then run `git rm -r --cached venv` and commit again. |
| `fatal: not a git repository` | You're in the wrong folder, or you haven't run `git init`. |

> 🧠 **Remember:** errors are not failures. Read the **last line** of the message, then search for it online. Thousands of people have had the same problem.
