from datetime import datetime
EXPENSE_FILE = "expense.txt"

def get_id(exp_record):
        if not exp_record: 
                return 1
        else:
            id_list = []
            for row in exp_record:
                   id_list.append(int(row[0])) 
            max_id = max(id_list)
            return max_id + 1

def validate_date(search_date):
        try:
             datetime.strptime(search_date,"%Y-%m-%d")
             return True
       
        except ValueError:
             print("Invalid Date Entry.")
             return False