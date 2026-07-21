import streamlit as st
from data.save_data import save_student
from utils.timetable import generate_timetable

st.title("🎓 Student Planner")

st.info(
    "💡 SmartLife Planner creates a balanced daily schedule by including "
    "sleep, meals, study, and at least 30 minutes of physical activity."
)


name = st.text_input("Name")
age = st.number_input("Age", min_value=10, max_value=100)
college = st.text_input("College")
department = st.text_input("Department")
gender = st.selectbox("Gender", ["Female", "Male", "Other"])

wake_up_time = st.time_input("Wake Up Time")

fresh_up_duration = st.slider(
    "🚿 Fresh Up Duration (minutes)",
    min_value=5,
    max_value=30,
    value=15
)

exercise_duration = st.slider(
    "🏃 Exercise Duration (minutes)",
    min_value=15,
    max_value=60,
    value=30
)

breakfast_duration = st.slider(
    "🍳 Breakfast Duration (minutes)",
    min_value=15,
    max_value=60,
    value=30
)

college_start_time = st.time_input("College Start Time")
college_end_time = st.time_input("College End Time")

home_study_hours = st.slider(
    "📚 Home Study Hours",
    min_value=0,
    max_value=6,
    value=2
)

dinner_duration = st.slider(
    "🍽 Dinner Duration (minutes)",
    min_value=15,
    max_value=60,
    value=30
)
relax_duration = st.slider(
    "🛋 Relaxation Time (minutes)",
    min_value=15,
    max_value=120,
    value=30
)
sleep_hours = st.slider(
    "😴 Preferred Sleep Hours",
    min_value=7,
    max_value=10,
    value=8
)
exercise = st.checkbox("I already exercise regularly")

student = {
    "name": name,
    "age": age,
    "college": college,
    "department": department,
    "gender": gender,
    "wake_up_time": str(wake_up_time),
    "fresh_up_duration": fresh_up_duration,
    "exercise_duration": exercise_duration,
    "breakfast_duration": breakfast_duration,
    "college_start_time": str(college_start_time),
    "college_end_time": str(college_end_time),
    "home_study_hours": home_study_hours,
    "dinner_duration": dinner_duration,
    "relax_duration": relax_duration,
    "sleep_hours": sleep_hours,
    "exercise": exercise
}

    

if st.button("Generate Timetable"):
    

    save_student(student)

    st.success("Student details saved successfully!")

    st.json(student)

    generate_timetable(
        wake_up_time,
        fresh_up_duration,
        exercise_duration,
        breakfast_duration,
        college_start_time,
        college_end_time,
        home_study_hours,
        dinner_duration,
        relax_duration,
        sleep_hours,
        exercise
    )