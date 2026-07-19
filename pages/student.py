import streamlit as st

st.title("🎓 Student Planner")

name = st.text_input("Name")
age = st.number_input("Age", min_value=10, max_value=100)

college = st.text_input("College")
department = st.text_input("Department")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
wake_up_time = st.time_input("Wake Up Time")
study_hours = st.slider("Study Hours", 0, 24, 8)
exercise = st.checkbox("Exercise")

student = {
    "name": name,
    "age": age,
    "college": college,
    "department": department,
    "gender": gender,
    "wake_up_time": str(wake_up_time),
    "study_hours": study_hours,
    "exercise": exercise
}

st.subheader("Student Details")

def generate_timetable(wake_up_time, study_hours, exercise):

    st.subheader("📅 Your Timetable")

    st.write(f"🌅 Wake Up: {wake_up_time}")
    st.write("🍳 Breakfast: 8:00 AM")
    st.write("🏫 College")
    st.write(f"📚 Study: {study_hours} hours")

    if study_hours < 7:
        st.warning("📚 Study at least 7 hours.")
    else:
        st.success("🎉 Great study schedule!")

    st.write(f"🏃 Exercise: {'Yes' if exercise else 'No'}")

    if exercise:
        st.success("🏃 Great! Keep exercising.")
    else:
        st.warning("⚠ Exercise for at least 30 minutes.")

    st.write("🍽 Dinner: 7:00 PM")
    st.write("😴 Sleep: 10:00 PM")


if st.button("Generate Timetable"):

    st.success("Student details saved successfully!")

    st.json(student)

    generate_timetable(wake_up_time, study_hours, exercise)