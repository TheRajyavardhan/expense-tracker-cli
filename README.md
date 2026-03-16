# Expense Tracker CLI

A modular **Command Line Expense Tracker** built with Python.
This application allows users to record, manage, and review their daily expenses through a simple and interactive terminal interface.

The project focuses on strengthening core Python concepts such as modular programming, file handling, input validation, and basic data manipulation using **Pandas**.

---

# Features

* Add new expense records
* View all stored expenses
* Search expenses by ID
* View expenses by date
* View expenses by category
* Update existing expense records
* Delete expense entries
* Calculate total spending
* Automatic ID generation
* Default date set to current day if left empty
* Input validation for amount, date, and category

---

# Project Structure

```
Expense-Tracker/

- main.py           --> Entry point of the application
- storage.py       --> Handles file operations (read/write/update)
- expense.py       --> Expense-related logic and data structure
- utils.py         --> Helper functions (validation, formatting)
- expenses.csv     --> Expense data storage (auto-created)
- README.md        -->Project documentation

```

**main.py**
Program entry point. Handles the user interface and menu system.

**expense_ops.py**
Contains the core business logic such as adding, updating, searching, and deleting expenses.

**storage.py**
Manages data storage and retrieval using CSV files through Pandas.

**utils.py**
Contains helper functions for validation and utility tasks such as generating IDs and validating input.

**expense.txt**
Stores all expense records.

---

# Technologies Used

* Python 3
* Pandas
* CSV File Storage
* Standard Python Libraries

No external database or frameworks are required.

---

# How the Program Works

1. The program displays a menu with different options.
2. The user selects an option by entering a number.
3. The program performs the requested operation.
4. Expense data is stored in a CSV file for persistence.

---

# Example Menu

```
========================================
            Expense Tracker
========================================
1. Add new expense
2. View all expense
3. View expenses by date
4. View expense by category
5. Search Expense ID
6. Update an expense
7. Delete an expense
8. Show total expense
9. Exit
========================================
```

---

# Example Expense Record

```
Id | Date       | Amount | Category | Note
------------------------------------------------
1  | 2026-03-16 | 250.0  | food     | vegetables
```

---

# Learning Objectives

This project was built to practice:

* Modular programming in Python
* File handling and persistent storage
* Data manipulation using Pandas
* Input validation and error handling
* Designing menu-driven CLI applications

---

# Future Improvements

Possible enhancements for future versions:

* Graphical user interface (Tkinter)
---

# Author

Developed as a Python practice project to improve programming fundamentals and build practical coding experience.



