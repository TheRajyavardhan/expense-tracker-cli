from utils import EXPENSE_FILE
import csv
import os


def insert_exp(exp_row, exp_file):
    try:
        with open(exp_file, "a", newline="") as file:
            csv.writer(file).writerows(exp_row)
        return True
    except FileNotFoundError:
        print("File not found.")
        return


def get_exp_list():
    try:
        rows = []
        with open(EXPENSE_FILE, "r") as file:
            rows = list(csv.reader(file))
            return rows
    except FileNotFoundError:
        print("File not found.")


def display_all_record():
    try:
        with open(EXPENSE_FILE, "r") as file:
            rows = list(csv.reader(file))
            if not rows:
                print("Empty Records.")
            else:
                for row in rows:
                    print()
                    print("ID: ", row[0])
                    print("Date: ", row[1])
                    print("Amount: ", row[2])
                    print("Category: ", row[3])
                    print("Note: ", row[4])
                    print()
        return
    except FileNotFoundError:
        print("File not found.")


def replace_file(new_file):
    os.replace(new_file, EXPENSE_FILE)
