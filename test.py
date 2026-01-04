# import datetime  as dt
# today = dt.date.today().isoformat()
# print(today)

import storage as st
import utils as ut

result = st.get_exp_list()
abs = ut.get_id(result)
print(abs)

final = st.insert_exp([6,2026-1-4,400,"Shopping","Clothing"])
print(final)