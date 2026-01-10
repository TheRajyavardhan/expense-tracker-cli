from datetime import datetime, date

EXPENSE_FILE = "expense.txt"


def get_id(exp_record):
    try:
        if not exp_record:
            return 1
        else:
            id_list = []
            for row in exp_record:
                id_list.append(int(row[0]))
            max_id = max(id_list)
            return max_id + 1
    except FileNotFoundError:
        print("File not found.")


def validate_date(search_date):
    try:
        entered_date = datetime.strptime(search_date, "%Y-%m-%d").date()
        if entered_date > date.today():
            return None
        return search_date
    except ValueError:
        return None


def find_unique_categories(exp_list):
    if not exp_list:
        print("No category.")
        return
    unique_list = {}
    idx = 0
    for row in exp_list:
        found = False
        if row[3] in unique_list.values():
            found = True
        if found:
            continue
        unique_list[idx] = row[3]
        idx += 1
    return unique_list


def validate_input(updated_entry, updated_var):
    if updated_var == "1":
        if validate_date(updated_entry):
            return True
    elif updated_var == "2":
        if valid_amount(updated_entry) != None:
            return True
    elif updated_var == "3":
        if valid_category(updated_entry):
            return True
    elif updated_var == "4":
        return True
    return False


def valid_amount(amount):
    try:
        amount = float(amount)
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
