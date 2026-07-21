import streamlit as st
from data.save_employee import save_employee
from utils.employee_timetable import generate_employee_timetable
st.title("💼 Employee Planner")

st.info(
    "💡 SmartLife Planner creates a balanced daily schedule by including "
    "sleep, meals, work, and physical activity."
)


st.subheader("👤 Personal Information")

name = st.text_input("Name")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

company = st.text_input("Company")

job_role = st.text_input("Job Role")


st.subheader("🌅 Morning Routine")

wake_up_time = st.time_input("Wake Up Time")

fresh_up_duration = st.slider(
    "🚿 Fresh Up Duration (minutes)",
    min_value=5,
    max_value=30,
    value=15,
)

exercise_duration = st.slider(
    "🏃 Exercise Duration (minutes)",
    min_value=15,
    max_value=60,
    value=30,
)

exercise = st.checkbox("I already exercise regularly")

breakfast_duration = st.slider(
    "🍳 Breakfast Duration (minutes)",
    min_value=15,
    max_value=60,
    value=30,
)


st.subheader("💻 Work Schedule")

work_start_time = st.time_input("Work Start Time")

work_end_time = st.time_input("Work End Time")


st.subheader("🌙 Evening Routine")

dinner_duration = st.slider(
    "🍽 Dinner Duration (minutes)",
    min_value=15,
    max_value=60,
    value=30,
)

relaxation_duration = st.slider(
    "🛋 Relaxation Time (minutes)",
    min_value=15,
    max_value=120,
    value=30,
)

sleep_hours = st.slider(
    "😴 Preferred Sleep Hours",
    min_value=7,
    max_value=10,
    value=8,
)

if st.button("Generate Timetable"):

    employee_data = {
        "name": name,
        "age": age,
        "gender": gender,
        "company": company,
        "job_role": job_role,
        "wake_up_time": str(wake_up_time),
        "fresh_up_duration": fresh_up_duration,
        "exercise_duration": exercise_duration,
        "exercise": exercise,
        "breakfast_duration": breakfast_duration,
        "work_start_time": str(work_start_time),
        "work_end_time": str(work_end_time),
        "dinner_duration": dinner_duration,
        "relaxation_duration": relaxation_duration,
        "sleep_hours": sleep_hours,
    }

    save_employee(employee_data)

    st.success("Employee details saved successfully!")
    st.json(employee_data)

    generate_employee_timetable(
        wake_up_time,
        fresh_up_duration,
        exercise_duration,
        breakfast_duration,
        work_start_time,
        work_end_time,
        dinner_duration,
        relaxation_duration,
        sleep_hours,
        exercise,
    )