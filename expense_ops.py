import storage as st
import utils as ut


def add_expense(date, amt, cate, note):
    amt = ut.valid_amount(amt)
    if amt == None:
        print("Invalid amount.")
        return
    if not ut.valid_category(cate):
        print("Invalid category.")
        return
    if ut.validate_date(date) == None:
        print("Invalid Date.")
        return
    exp_record = st.get_exp_list()
    id = ut.get_id(exp_record)
    exp_row = [id, date, amt, cate, note]
    return st.insert_exp([exp_row], "expense.txt")


def view_all_record():
    st.display_all_record()


def search_exp_id(search_id):
    exp_list = st.get_exp_list()

    if not exp_list:
        print("Empty Record.")
        return
    for row in exp_list:
        if row[0] == search_id:
            print("Date: ", row[1])
            print("Amount: ", row[2])
            print("Category: ", row[3])
            print("Note: ", row[4])
            return
    print("Expense ID not found.")


def exp_by_date(search_date):

    if not ut.validate_date(search_date):
        print("Invalid date entry.")
        return

    exp_list = st.get_exp_list()
    found = False

    if not exp_list:
        print("Empty Record.")
        return
    for row in exp_list:
        if row[1] == search_date:
            print()
            print("ID: ", row[0])
            print("Amount: ", row[2])
            print("Category: ", row[3])
            print("Note: ", row[4])
            print()
            found = True
    if not found:
        print("Date not found.")
    return


def exp_by_category():
    exp_list = st.get_exp_list()
    category_list = ut.find_unique_categories(exp_list)
    print("Choose the category: ")

    for key, val in category_list.items():
        option_line = str(key + 1) + ". " + val
        print(option_line)
    idx = input("Enter the category: ")
    for row in exp_list:
        if row[3] == category_list[int(idx) - 1]:
            print("\nExpense ID: ", row[0])
            print("Date: ", row[1])
            print("Amount: ", row[2])
            print("Note: ", row[4], end="\n\n")


def update_exp(search_id, update_var):
    exp_list = st.get_exp_list()
    new_exp_list = []
    field_list = ["date", "amount", "category", "note"]
    for row in exp_list:
        if row[0] == search_id:
            print("Enter your updated", field_list[int(update_var) - 1], end="")
            print(": ", end="")
            updated_entry = input().lower()
            if not ut.validate_input(updated_entry, update_var):
                print("Invalid Entry.")
                return
            if update_var == "2":
                updated_entry = float(updated_entry)
            row[int(update_var)] = updated_entry
        new_exp_list.append(row)
    temp_file = "temp.txt"
    st.insert_exp(new_exp_list, temp_file)
    st.replace_file(temp_file)


def delete_exp_id(search_id):
    exp_list = st.get_exp_list()
    new_exp_list = []
    for row in exp_list:
        if row[0] == search_id:
            continue
        new_exp_list.append(row)
    temp_file = "temp.txt"
    st.insert_exp(new_exp_list, temp_file)
    st.replace_file(temp_file)


def total_expense():
    exp_list = st.get_exp_list()
    total_exp = 0
    for row in exp_list:
        total_exp += float(row[2])
    print("Total Expense: ", total_exp)
