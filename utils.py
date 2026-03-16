from datetime import datetime, date
import pandas as pd

EXPENSE_FILE = "expense.txt"


def get_id():
    try:
        df = pd.read_csv(EXPENSE_FILE) # load data from expense file as DataFrame
        max_id = df["Id"].max() # find max value in id column
        return max_id + 1
    except FileNotFoundError:
        return 1


def validate_date(search_date):
    try:
        if search_date == "":
            search_date = date.today().isoformat() # Make default value equal current date
        entered_date = datetime.strptime(search_date, "%Y-%m-%d").date() # check correct format for date
        if entered_date > date.today(): # check if date is not in future
            return None
        return search_date
    except ValueError:
        return None


def find_unique_categories(exp_list):
    unique_cate = exp_list["Category"].unique() # find all value in category column of DataFrame
    return unique_cate


def valid_input(updated_entry, updated_var):
    if updated_var == "Date":
        if validate_date(updated_entry) is not None:
            return True
    elif updated_var == "Amount":
        if valid_amount(float(updated_entry)) is not None:
            return True
    elif updated_var == "Category":
        if valid_category(updated_entry):
            return True
    elif updated_var == "Note":
        return True
    return False


def valid_amount(amount):
    try:
        if amount <= 0:
            raise ValueError
        return amount

    except ValueError:
        return None


def valid_category(cate):
    if len(cate) < 3:
        return False
    for ch in cate:
        if not (ch.isalpha() or ch in " #&"):
            return False
    return True
