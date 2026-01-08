import expense_ops as eo
# import datetime 
import datetime
def main():

    do_stop = False
    while do_stop != True:

        print("======== Expense Tracker ========")
        print("1. Add new expense")
        print("2. View all expense")
        print("3. Viw expenses by date")
        print("4. View expense by category")
        print("5. Search Expense ID.")
        print("6. Update an expense")
        print("7. Delete an expense")
        print("8. Show total expense")
        print("9. Exit")
        print("=================================")

        selected_opt = int(input("Your choice: "))

        if selected_opt == 1:
            stop_adding = False
            while stop_adding != True:
                amt = input("Enter the amount: ")
                if not amt.isdigit() or int(amt) <= 0:
                    print("Invalid Amount.")
                    break
                category = input("Enter the category: ").strip().lower()
                if not category.isalpha():
                    print("Invalid Category.")
                    break
                exp_date = datetime.date.today().isoformat()
                note = input("Enter the note: ")
                result = eo.add_expense(amt,category,exp_date,note)
                if result == True:
                    print("Expenses added successfully.")
                ans = input("Do you want to continue adding expense? (Enter = yes, n = no)... ").lower()
                if ans == 'n':
                    stop_adding = True

        elif selected_opt == 2:
            eo.view_all_record()
        
        elif selected_opt == 3:
            exp_date = input("Enter the date(YYYY-MM-DD): ")
            eo.exp_by_date(exp_date)

        elif selected_opt == 4:
             eo.exp_by_category()

        elif selected_opt == 5:
            search_id = input("Enter the Expense ID: ")
            if not search_id.isdigit():
                print("Invalid ID Entry.")
            eo.search_exp_id(search_id)

        elif selected_opt == 6:
            stop_updating = False
            while not stop_updating:
                search_id = input("Enter the Expense ID: ")
                if not search_id.isdigit():
                    print("Invalid ID Entry.")
                    continue
                stop_opt = False
                while not stop_opt:
                    update_var = input(
                            "Update Expense:\n"
                            "1. Date\n"
                            "2. Amount\n"
                            "3. Category\n"
                            "4. Note\n"
                            "0. Cancel\n"
                            "Enter your choice: ")
                    if update_var == '0':  
                        stop_opt = True
                    elif update_var not in ('1','2','3','4'):
                        print("Invalid choice.")
                    else:
                        eo.update_exp(search_id,update_var)

                temp = input(
                    "Do you want to update more records? (Enter = yes, n=no).... "
                    ).lower()
                if temp == 'n':
                    stop_updating = True
                    break
        
        
        elif selected_opt == 7:
            stop_deleting = False
            while not stop_deleting:
                search_id = input("Enter the Expense ID: ")
                if not search_id.isdigit():
                    print("Invalid ID Entry.")
                eo.delete_exp_id(search_id)
                ans = input("Do you want to delete more expense? (Enter = yes, n = no)...").lower()
                if ans == 'n':
                    stop_deleting = True
                    break
        
        elif selected_opt == 8:
            eo.total_expense()

        elif selected_opt == 9:
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