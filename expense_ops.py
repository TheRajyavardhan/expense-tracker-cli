import storage as st
import utils as ut


def add_expense(amt,cate,date,note):
    exp_record = st.get_exp_list()
    id = ut.get_id(exp_record)
    exp_list = [id,amt,date,cate,note] 
    return st.insert_exp(exp_list)

