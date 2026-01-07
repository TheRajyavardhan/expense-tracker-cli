# import datetime  as dt
# today = dt.date.today().isoformat()
# print(today)

# import storage as st
import utils as ut

# result = st.get_exp_list()
# abs = ut.get_id(result)
# print(abs)

# final = st.insert_exp([6,2026-1-4,400,"Shopping","Clothing"])
# print(final)

from utils import EXPENSE_FILE
# with open(EXPENSE_FILE, "rb") as f:
#     print(f.read())

# import storage as st
# result = st.get_exp_list()
# print(result)

# exp_id = ut.get_id(result)
# print(exp_id)
# def get_id(exp_record):
#         if not exp_record: 
#                 print(exp_record)
#                 return 1
#         else:
#             id_list = []
#             for row in exp_record:
#                    id_list.append(int(row[0])) 
#             max_id = max(id_list)
#             print(id_list)
#             return max_id + 1

# exp_id = get_id(result)
# print("Exp. ID: ",exp_id)
import csv

# def display_all_record():
#     try:
#         with open(EXPENSE_FILE,"r") as file:
#             rows = list(csv.reader(file))
#             if not rows:
#                 print("Empty Records.")
#             else:
#                 for row in rows:
#                     print()
#                     print("ID: ",row[0])
#                     print("Date: ",row[1])
#                     print("Amount: ", row[2])
#                     print("Category: ", row[3])
#                     print("Note: ", row[4])
#                     print()
#         return
#     except FileNotFoundError:
#         print("File not found.") 

# display_all_record()

import storage as st
# exp_list = st.get_exp_list()
# unique_list = ut.find_unique_categories(exp_list)
# print(unique_list)
# for k,v in unique_list:
#     print(k,v)
import expense_ops as eo

eo.show_all_category()