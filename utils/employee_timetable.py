import streamlit as st
from datetime import datetime, timedelta

from utils.employee_validation import (
    validate_work_time,
    validate_wake_up_time,
    validate_morning_schedule,
    validate_evening_schedule,
)

from utils.employee_health import show_employee_health_summary


def generate_employee_timetable(
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
):
    wake = datetime.combine(datetime.today(), wake_up_time)
    work_start = datetime.combine(datetime.today(), work_start_time)
    work_end = datetime.combine(datetime.today(), work_end_time)

    fresh_up_start = wake
    fresh_up_end = fresh_up_start + timedelta(minutes=fresh_up_duration)

    exercise_start = fresh_up_end
    exercise_end = exercise_start + timedelta(minutes=exercise_duration)

    breakfast_start = exercise_end
    breakfast_end = breakfast_start + timedelta(minutes=breakfast_duration)

    recommended_bed_time = wake + timedelta(days=1) - timedelta(hours=sleep_hours)
    relax_end = recommended_bed_time
    relax_start = relax_end - timedelta(minutes=relaxation_duration)

    dinner_end = relax_start
    dinner_start = dinner_end - timedelta(minutes=dinner_duration)

    if not validate_work_time(work_start, work_end):
        return
    if not validate_wake_up_time(wake, work_start):
        return
    if not validate_morning_schedule(breakfast_end, work_start):
        return
    if not validate_evening_schedule(dinner_start, work_end):
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
        f"💼 Work : {work_start.strftime('%I:%M %p')} - "
        f"{work_end.strftime('%I:%M %p')}"
    )
    st.write(
        f"🍽 Dinner : {dinner_start.strftime('%I:%M %p')} - "
        f"{dinner_end.strftime('%I:%M %p')}"
    )

    st.write(
        f"🛋 Relaxation : {relax_start.strftime('%I:%M %p')} - "
        f"{relax_end.strftime('%I:%M %p')}"
    )

    st.write(
        f"😴 Sleep : {recommended_bed_time.strftime('%I:%M %p')}"
    )

    show_employee_health_summary(
    exercise,
    sleep_hours,
    )