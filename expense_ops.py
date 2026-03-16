import storage as st
import utils as ut


def add_expense(amt, cate, note, date):
    amt = ut.valid_amount(amt) # check amount values
    if amt is None:
        print("Invalid amount.Enter the positive number.")
        return
    if not ut.valid_category(cate): # checking the category entry
        print("Invalid category.")
        return
    date = ut.validate_date(date) # checking the date entry
    if date is None:
        print("Invalid Date.")
        return
    id = ut.get_id() # return unique id number
    exp_row = [id, date, amt, cate, note]
    return st.insert_exp(exp_row) # insert new record into csv file


def view_all_record():
    exp_list = st.get_exp_list() # load all expense data in DataFrame structure
    if not exp_list.empty:
        print(exp_list.to_string(index=False)) # index won't print
    else:
        print("No records found.")


def search_exp_id(search_id):

    exp_list = st.get_exp_list()
    if exp_list.empty: # checking expense file is empty/not exist.
        print("No record found.")
        return
    match = exp_list[exp_list["Id"] == search_id] # created a mask for finding the id.
    if not match.empty:
        print("\n", match.to_string(index=False))
        return
    print("Expense ID not found.")


def exp_by_date(search_date):

    search_date = ut.validate_date(search_date)
    if not search_date:
        print("Invalid date entry.")
        return

    exp_list = st.get_exp_list()
    if exp_list.empty:
        print("No records found.")
        return
    match = exp_list[exp_list["Date"] == search_date]
    if not match.empty:
        print("\n", match.to_string(index=False))
        return
    print("Specified date not found.")


def exp_by_category():

    exp_list = st.get_exp_list()
    if exp_list.empty:
        print("No records found.")
        return
    category_list = ut.find_unique_categories(exp_list) # return a list of categories available
    print("Choose the category: ")

    key = 1
    for val in category_list:
        option_line = str(key) + ". " + val
        print(option_line)
        key += 1
    idx = int(input("Enter the category: ")) - 1
    match = exp_list[exp_list["Category"] == category_list[idx]]
    print("\n", match.to_string(index=False))


def update_exp(search_id, update_var):

    exp_list = st.get_exp_list()
    if exp_list.empty:
        print("No record found.")
        return True
    mask = exp_list["Id"] == search_id
    if mask.any():
        updated_entry = input("Enter the updated value: ")
        if not ut.valid_input(updated_entry, update_var):
            print("Not valid entry.")
            return False
        if update_var == "Amount": 
            updated_entry = float(updated_entry) # turn string to float value
        exp_list.loc[mask, update_var] = updated_entry
        st.save_list(exp_list) # overwrite the existing file with updated data
        print("Record updated.")
        return False
    print("Id not found.")
    return True


def delete_exp_id(search_id):

    exp_list = st.get_exp_list()
    if exp_list.empty:
        print("No records found.")
        return
    mask = exp_list["Id"] == search_id
    if mask.any():
        ask = input("Are you sure? (Enter = yes,n = no)...").strip().lower()
        if ask == "no":
            print("Deletiton cancelled.")
            return
        exp_list.drop(exp_list[mask].index, inplace=True) # deleting the record/row
        st.save_list(exp_list)
        print("ID deleted successfully.")
        return
    print("Id not found.")
    return


def total_expense():

    exp_list = st.get_exp_list()
    if exp_list.empty:
        print("No records found.")
        return
    print("Total Expense: ", exp_list["Amount"].sum())
