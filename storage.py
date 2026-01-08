from utils import EXPENSE_FILE
import csv

def insert_exp(exp_list,exp_file):
    try: 
        with open(exp_file,"a",newline="") as file:
            csv.writer(file).writerow(exp_list)
        return True
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
    
def display_all_record():
    try:
        with open(EXPENSE_FILE,"r") as file:
            rows = list(csv.reader(file))
            if not rows:
                print("Empty Records.")
            else:
                for row in rows:
                    print()
                    print("ID: ",row[0])
                    print("Date: ",row[1])
                    print("Amount: ", row[2])
                    print("Category: ", row[3])
                    print("Note: ", row[4])
                    print()
        return
    except FileNotFoundError:
        print("File not found.") 

def update_exp_record(search_id):
    exp_list = get_exp_list()




