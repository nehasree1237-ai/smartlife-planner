import streamlit as st

st.title("💼 Employee Planner")

name = st.text_input("Name")
age = st.number_input("Age", min_value=18, max_value=100)

job = st.text_input("Job Role")
company = st.text_input("Company")
if st.button("Generate Schedule"):
   if(
     name.lower()=="avinash"
     and age==27
     and job.lower()=="specialist programmer"
     and company.lower()=="infosys"
  ):
     st.success("welcome bangaramm")
   else:    
     st.success(f"Welcome {name}!")