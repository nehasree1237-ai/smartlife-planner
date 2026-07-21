import streamlit as st
from datetime import datetime, timedelta
from utils.health import show_health_summary
from utils.validation import (
    validate_schedule,
    validate_college_time,
    validate_wake_up_time,
    validate_evening_schedule,
)


def generate_timetable(
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
    exercise,
):
    wake = datetime.combine(datetime.today(), wake_up_time)
    college_start = datetime.combine(datetime.today(), college_start_time)
    college_end = datetime.combine(datetime.today(), college_end_time)

    fresh_up_start = wake
    fresh_up_end = fresh_up_start + timedelta(minutes=fresh_up_duration)

    exercise_start = fresh_up_end
    exercise_end = exercise_start + timedelta(minutes=exercise_duration)

    breakfast_start = exercise_end
    breakfast_end = breakfast_start + timedelta(minutes=breakfast_duration)

    recommended_bed_time = wake + timedelta(days=1) - timedelta(hours=sleep_hours)
    relax_end = recommended_bed_time
    relax_start = relax_end - timedelta(minutes=relax_duration)

    dinner_end = relax_start
    dinner_start = dinner_end - timedelta(minutes=dinner_duration)

    study_end = dinner_start
    study_start = study_end - timedelta(hours=home_study_hours)

    if not validate_college_time(college_start, college_end):
        return
    if not validate_wake_up_time(wake, college_start):
        return
    if not validate_schedule(breakfast_end, college_start):
        return
    if not validate_evening_schedule(study_start, college_end):
        return

    st.subheader("📅 Your Timetable")

    st.write(f"🌅 Wake Up : {wake.strftime('%I:%M %p')}")

    st.write(
        f"🚿 Fresh Up : {fresh_up_start.strftime('%I:%M %p')} - "
        f"{fresh_up_end.strftime('%I:%M %p')}"
    )

    st.write(
        f"🏃 Exercise : {exercise_start.strftime('%I:%M %p')} - "
        f"{exercise_end.strftime('%I:%M %p')}"
    )

    st.write(
        f"🍳 Breakfast : {breakfast_start.strftime('%I:%M %p')} - "
        f"{breakfast_end.strftime('%I:%M %p')}"
    )

    st.write(
        f"🏫 College : {college_start.strftime('%I:%M %p')} - "
        f"{college_end.strftime('%I:%M %p')}"
    )

    st.write(
        f"📚 Home Study : {study_start.strftime('%I:%M %p')} - "
        f"{study_end.strftime('%I:%M %p')}"
    )

    st.write(
        f"🍽 Dinner : "
        f"{dinner_start.strftime('%I:%M %p')} - "
        f"{dinner_end.strftime('%I:%M %p')}"
    )
    st.write(f"😴 Sleep : {recommended_bed_time.strftime('%I:%M %p')}")

    show_health_summary(home_study_hours, exercise, sleep_hours)
