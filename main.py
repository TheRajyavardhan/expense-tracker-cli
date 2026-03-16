import expense_ops as eo


# -------------------------------
# Safe input functions
# -------------------------------


def get_int(prompt): # avoid value error for int input
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter a number.")


def get_float(prompt): # avoid value error for float input
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid amount. Enter a numeric value.")


# -------------------------------
# Menu wrapper functions
# -------------------------------


def add_expense_menu(): # Menu for expense addition
    amt = get_float("Enter the amount: ")
    category = input("Enter the category: ").strip().lower()
    exp_date = input("Enter the date (YYYY-MM-DD) [default: today]: ")
    note = input("Enter the note: ").lower().strip()
    eo.add_expense(amt, category, note, exp_date)


def view_by_date_menu():
    exp_date = input("Enter the date (YYYY-MM-DD) [default: today]: ")
    eo.exp_by_date(exp_date)


def search_menu():
    search_id = get_int("Enter the Expense ID: ")
    eo.search_exp_id(search_id)


def update_menu(): # Menu for updating expense record
    search_id = get_int("Enter the Expense ID: ")

    print("\nUpdate Expense")
    print("1. Date")
    print("2. Amount")
    print("3. Category")
    print("4. Note")
    print("0. Cancel")

    choice = get_int("Enter your choice: ")

    if choice == 0:
        return

    if choice not in (1, 2, 3, 4):
        print("Invalid option.")
        return

    fields = ["", "Date", "Amount", "Category", "Note"]

    eo.update_exp(search_id, fields[choice])


def delete_menu():
    search_id = get_int("Enter the Expense ID: ")
    eo.delete_exp_id(search_id)


# -------------------------------
# Menu dictionary
# -------------------------------

menu = {
    1: add_expense_menu,
    2: eo.view_all_record,
    3: view_by_date_menu,
    4: eo.exp_by_category,
    5: search_menu,
    6: update_menu,
    7: delete_menu,
    8: eo.total_expense,
}


# -------------------------------
# Main program
# -------------------------------


def main():

    while True:

        print("=" * 40)
        print("            Expense Tracker")
        print("=" * 40)
        print("1. Add new expense")
        print("2. View all expense")
        print("3. View expenses by date")
        print("4. View expense by category")
        print("5. Search Expense ID")
        print("6. Update an expense")
        print("7. Delete an expense")
        print("8. Show total expense")
        print("9. Exit")
        print("=" * 40)

        choice = get_int("Your choice: ")

        if choice == 9:
            print("Program terminated.")
            break

        action = menu.get(choice) # 'get' return value corresponding to key

        if action: # action = f
            action() # action() = f()
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
