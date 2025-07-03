
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


if "expense_data" not in st.session_state:
    st.session_state.expense_data=pd.DataFrame(columns=["Date","Category","Amount","Description"])

def add_expense(date,category,amount,description):
    st.session_state.new_expense=pd.DataFrame([[date,category,amount,description]],columns=st.session_state.expense_data.columns)
    st.session_state.expense_data=pd.concat([st.session_state.expense_data,st.session_state.new_expense],ignore_index=True)

def load_expense():
     uploaded_file=st.file_uploader("Uplode a file",type=["csv"])
     if uploaded_file is not None:
          st.session_state.expense_data=pd.read_csv(uploaded_file)

def save_expense():
     st.session_state.expense_data.to_csv('expense_data.csv',index=False)
     st.success("Expenses saved successfully")

def visual():
     if not st.session_state.expense_data.empty:
          fig,ax=plt.subplots()
          sns.barplot(data=st.session_state.expense_data,x="Category",y="Amount",ax=ax)
          plt.xticks(rotation=45)
          st.pyplot(fig)
     else:
          st.warning("No Expense to visualize")


st.title("Expense Tracker")
with st.sidebar:
    st.header("Add Expense")
    date=st.date_input("Date")
    category=st.selectbox("Category",['Food','Travel','Entetainment','Utilities','Others'])
    amount=st.number_input('Amount',min_value=0.0,format="%.2f")
    description=st.text_input('Description')
    if st.button("Add"):
        add_expense(date,category,amount,description)
        st.success("Expenses Added successfully!")
        
    st.header('File Operation')
    if st.button('Save Expenses'):
        save_expense()

    if st.button('Load Expenses'):
        load_expense()

st.header("Expenses")
st.write(st.session_state.expense_data)

st.header("Visualization")
if st.button('Visualizaation'):
            visual()

