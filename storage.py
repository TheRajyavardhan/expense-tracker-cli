from utils import EXPENSE_FILE
import os
import pandas as pd


def insert_exp(exp_row):
    df = pd.DataFrame([exp_row], columns=["Id", "Date", "Amount", "Category", "Note"])
    if not os.path.exists(EXPENSE_FILE) or os.path.getsize(EXPENSE_FILE) == 0: # check file is existing or not. Also check if it's empty
        df.to_csv(EXPENSE_FILE, mode="w", index=False, header=True) # create new file for records
    else:
        df.to_csv(EXPENSE_FILE, mode="a", index=False, header=False) # write into existing file
    print("Expense record added successfully.")
    return


def get_exp_list():
    try:
        exp_list = pd.read_csv(EXPENSE_FILE) # return all data from record file as DataFrame
        return exp_list
    except (FileNotFoundError, pd.errors.EmptyDataError):
        exp_list = pd.DataFrame(columns=["Id", "Date", "Amount", "Category", "Note"])
        return exp_list


def save_list(new_list):
    new_list.to_csv(EXPENSE_FILE, index=False, header=True) # Save whole DataFrame into record file.
    return
