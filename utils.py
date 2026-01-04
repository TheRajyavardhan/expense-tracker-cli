EXPENSE_FILE = "expense.txt"

def get_id(exp_record):
        if len(exp_record) == 0: 
                return 1
        else:
            id_list = []
            for row in exp_record:
                   id_list.append(int(row[0])) 
            max_id = max(id_list)
            return max_id + 1
        