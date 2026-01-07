import storage as st
import utils as ut


def add_expense(amt,cate,date,note):
    exp_record = st.get_exp_list()
    id = ut.get_id(exp_record)
    exp_list = [id,date,amt,cate,note] 
    return st.insert_exp(exp_list)

def view_all_record():
    st.display_all_record()

def search_exp_id(search_id):
    exp_list = st.get_exp_list()
    
    if not exp_list:
        print("Empty Record.")
        return 
    for row in exp_list:
        if row[0] == search_id:
            print("Date: ",row[1])
            print("Amount: ",row[2])
            print("Category: ",row[3])
            print("Note: ",row[4])
            return
    print("Expense ID not found.")

def exp_by_date(search_date):
    
    if not ut.validate_date(search_date):
        print("Invalid Input")
        return 
    
    exp_list = st.get_exp_list()
    found = False

    if not exp_list:
        print("Empty Record.")
        return
    for row in exp_list:
        if row[1] == search_date:
            print()
            print("ID: ",row[0])
            print("Amount: ",row[2])
            print("Category: ",row[3])
            print("Note: ",row[4])
            print()
            found = True
    if not found:
        print("Date not found.")
    return 

def exp_by_category():
    exp_list = st.get_exp_list()
    category_list = ut.find_unique_categories(exp_list)
    print("Choose the category: ")

    for key,val in category_list.items():
        option_line = str(key+1)+". "+val
        print(option_line)
    idx = input("Enter the category: ")
    for row in exp_list:
        if row[3] == category_list[int(idx)-1]:
            print("\nExpense ID: ",row[0])
            print("Date: ",row[1])
            print("Amount: ",row[2])
            print("Note: ",row[4],end='\n\n')
    