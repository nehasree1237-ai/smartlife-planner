import streamlit as st

# Configure the page
st.set_page_config(
    page_title="SmartLife Planner",
    page_icon="🧠",
    layout="centered"
)

# Title
st.title("🧠 SmartLife Planner")

# Welcome message
st.write("## Welcome!")
st.write("Choose your profile to continue:")

# Create two columns for buttons
col1, col2 = st.columns(2)

# Student button
with col1:
    if st.button("🎓 Student"):
        st.switch_page("pages/student.py")

# Employee button
with col2:
    if st.button("💼 Employee"):
        st.switch_page("pages/employee.py")
        