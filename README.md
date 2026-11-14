# 🐍 Python Course

Welcome! This repository holds everything for our Python course: notes, assignments, guided projects, quizzes and the course plan.

## 📁 What's where

```text
python-course/
├── README.md                      ← you are here (course roadmap)
├── Python_Course_Notes/           ← the 8 topic notebooks (study these!)
│   └── 00_Developer_Tools_Guide.md    ← Git, GitHub, pip, virtual environments
├── Assignments/
│   ├── Assignment_Descriptions/   ← Python_Assignment_1 ... 6
│   └── Assignment_Solutions/      ← answer keys (instructor)
├── Projects/
│   ├── Project_Descriptions/      ← guided project workbooks
│   └── Project_Solutions/         ← complete project code
├── Quiz/                          ← quizzes
├── Teaching_Plan/                 ← lecture plans (instructor)
└── Student_Submitted_Work/        ← one folder per student, checked and graded work
```

## 🚀 How to study

1. After each class, read the matching notebook in `Python_Course_Notes/` and **run every cell**.
2. Do the **✏️ Try it yourself** cells and the practice problems at the end of each notebook.
3. Do the assignment for that topic from `Assignments/Assignment_Descriptions/`.
4. Build the guided projects in `Projects/Project_Descriptions/`.
5. Commit your work to **your own** GitHub repository regularly.

New to Git, `pip` or virtual environments? Read [`00_Developer_Tools_Guide.md`](Python_Course_Notes/00_Developer_Tools_Guide.md).

---

## 🗺️ Course roadmap

✅ = covered in class   ⬜ = coming up

### Phase 1: Foundations
- [x] Orientation, how Python works, `print()` and comments
- [x] Variables, data types, `input()` and type conversion
- [x] Operators and numbers
- [x] Booleans, comparisons, `and` / `or` / `not`
- [x] Conditionals: `if` / `elif` / `else`, nested `if`, one-line `if`
- [x] `match` / `case`
- [x] Loops: `while`, `for`, `range()`, `break`, `continue`, nested loops
- [x] The `sys` and `random` modules
- [x] Git and GitHub introduction

📖 Notes: [`01_Python_Basics_and_Control_Flow`](Python_Course_Notes/01_Python_Basics_and_Control_Flow.ipynb)

### Phase 2: Data structures
- [x] Lists and list comprehensions
- [x] Strings and f-strings
- [x] Tuples and unpacking
- [x] Dictionaries
- [x] Sets

📖 Notes: [`02_Lists_Strings_Tuples`](Python_Course_Notes/02_Lists_Strings_Tuples.ipynb) · [`03_Dictionaries_and_Sets`](Python_Course_Notes/03_Dictionaries_and_Sets.ipynb)

### Phase 3: Functions, files and errors
- [x] Functions: parameters, `return`, default arguments, scope
- [x] `*args` and `**kwargs`
- [x] Lambda functions
- [x] Recursion
- [x] File handling and JSON
- [x] Exception handling: `try` / `except` / `else` / `finally` / `raise`

📖 Notes: [`04_Functions`](Python_Course_Notes/04_Functions.ipynb) · [`05_Files_and_Exceptions`](Python_Course_Notes/05_Files_and_Exceptions.ipynb)

### Phase 4: Object-Oriented Programming
- [x] Classes and objects, `__init__`, `self`, `__str__`
- [x] Class attributes vs instance attributes
- [x] Composition
- [x] Encapsulation
- [x] Inheritance and `super()`
- [x] Polymorphism and duck typing
- [x] Overriding vs overloading, `__eq__`
- [x] OOP extras: `@property`, `__repr__`, `isinstance()`, `@classmethod` / `@staticmethod`

📖 Notes: [`06_OOP_Part1_Classes_and_Objects`](Python_Course_Notes/06_OOP_Part1_Classes_and_Objects.ipynb) · [`07_OOP_Part2_Inheritance_and_Beyond`](Python_Course_Notes/07_OOP_Part2_Inheritance_and_Beyond.ipynb)

### Phase 5: Tools and the outside world
- [x] Modules: your own files, `import`, `if __name__ == "__main__"`
- [x] `pip`, virtual environments and `requirements.txt`
- [x] APIs with `requests`
- [ ] `datetime` (introduced inside a project)
- [ ] `@dataclass` *(optional)*

📖 Notes: [`08_APIs_with_requests`](Python_Course_Notes/08_APIs_with_requests.ipynb) · [`00_Developer_Tools_Guide.md`](00_Developer_Tools_Guide.md)

### Phase 6: Desktop apps (GUI)
- [ ] Tkinter core: windows, labels, buttons, `Entry`, `grid`, event handling
- [ ] A Library GUI that reuses our existing classes
- [ ] CustomTkinter *(optional bonus)*

### Phase 7: Databases
- [ ] `sqlite3`: tables, `INSERT`, `SELECT`, `UPDATE`, `DELETE`
- [ ] Connecting a project to a database

### Phase 8: The web
- [ ] HTML, CSS and JavaScript basics
- [ ] FastAPI: building our own API

### Phase 9: Capstone and specialization
- [ ] Capstone project
- [ ] Specialization tracks, chosen by each student's interests

---

## 🛠️ Guided projects

Workbooks live in `Projects/Project_Descriptions/`.

- [x] Workbook 1 (add `Python_Mini_Projects_Guided_Student_Workbook_1.docx` to `Project_Descriptions/`)
- [x] Workbook 2: first guided projects
- [x] Workbook 3: `*args` / `**kwargs`, lambda, recursion, exceptions, file handling
- [x] **Workbook 4**, Project 1: Library, Part 1 and Part 2
- [x] **Workbook 4**, Project 2: PySafe v2 (bank accounts)
- [ ] **Workbook 4**, Project 3: Text Battle Arena

## 📝 Assignments and quizzes

Assignments live in `Assignments/Assignment_Descriptions/`.

| Assignment | Topic |
|---|---|
| `Python_Assignment_1` | Variables, data types, input, operators, conditionals |
| `Python_Assignment_2` | Loops and lists, plus a review of strings and modules |
| `Python_Assignment_3` | Data structures: lists, tuples, dictionaries, sets |
| `Python_Assignment_4` | `*args` / `**kwargs`, lambda, recursion, exceptions, file handling |
| `Python_Assignment_5` | OOP: classes, class vs instance attributes, composition, encapsulation, `@property` |
| `Python_Assignment_6` | OOP: inheritance, polymorphism, `__eq__` / `__repr__`, `isinstance`, `@classmethod` |

Quiz: `Quiz/Python_Quiz_Conditionals_Loops.docx`

---

## 💡 Tips for success

- **Type the code yourself** instead of copy-pasting.
- **Predict the output** before you run a cell. If you're wrong, find out why.
- **Read the last line** of an error message first. Errors are information, not failure.
- **Commit often.** Your GitHub profile becomes your portfolio.
- Use the free **Kaggle "Python" course** as extra reading.
