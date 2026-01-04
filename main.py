import expense_ops as eo
from datetime import date
def main():

    do_stop = False
    while do_stop != True:

        print("======== Expense Tracker ========")
        print("1. Add new expense")
        print("2. View all expense")
        print("3. Viw expenses by date")
        print("4. View expense by category")
        print("5. Update an expense")
        print("6. Delete an expense")
        print("7. Show total expense")
        print("8. Exit")
        print("=================================")

        selected_opt = int(input("Your choice: "))

        if selected_opt == 1:
            stop_adding = False
            while stop_adding != True:
                amt = input("Enter the amount: ")
                if not amt.isdigit() or int(amt) <= 0:
                    print("Invalid Amount.")
                    break
                category = input("Enter the category: ")
                if not category.isalpha():
                    print("Invalid Category.")
                    break
                exp_date = date.today().isoformat()
                note = input("Enter the note: ")
                result = eo.add_expense(amt,category,exp_date,note)
                if result == 0:
                    print("Expenses added successfully.")
                ans = input("Do you want to continue adding expense? (Enter = yes, n = no)... ").lower()
                if ans == 'n':
                    stop_adding = True

        # elif selected_opt == 2:

        # elif selected_opt == 3:

        # elif selected_opt == 4:

        # elif selected_opt == 5:

        # elif selected_opt == 6:

        # elif selected_opt == 7:

        elif selected_opt == 8:
            ans = input(
                "Do you want to terminate this program? (Enter = yes, n = no).... "
            ).lower()
            if ans == "n":
                continue
            else:
                do_stop = True
        else:
            print("Invalid response. Try again")

if __name__ == "__main__":
    main()