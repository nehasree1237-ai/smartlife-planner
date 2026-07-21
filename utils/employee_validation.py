import streamlit as st


def validate_work_time(work_start, work_end):
    if work_end <= work_start:
        st.error("⚠ Work end time must be after work start time.")
        return False

    return True


def validate_wake_up_time(wake, work_start):
    if wake >= work_start:
        st.error("⚠ Wake-up time must be before work starts.")
        return False

    return True


def validate_morning_schedule(breakfast_end, work_start):
    if breakfast_end > work_start:
        st.error(
            "⚠ Your morning routine doesn't fit before work starts."
        )
        return False

    return True
def validate_evening_schedule(dinner_start, work_end):
    if dinner_start < work_end:
        st.error(
            "⚠ Your evening schedule doesn't fit after work. "
            "Reduce dinner or relaxation time."
        )
        return False

    return True


