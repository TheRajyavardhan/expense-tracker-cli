from utils import EXPENSE_FILE
import csv

def insert_exp(exp_list):
    try: 
        with open(EXPENSE_FILE,"a",newline="") as file:
            csv.writer(file).writerow(exp_list)
        return 0
    except FileNotFoundError:
        print("File not found.")
        return 

def get_exp_list():
    try:
        rows = []
        with open(EXPENSE_FILE,"r") as file:
            rows = list(csv.reader(file)) 
            return rows
    except FileNotFoundError:
        print("File not found.")
    

