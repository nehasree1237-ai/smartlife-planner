import streamlit as st


def validate_schedule(breakfast_end, college_start):
    if breakfast_end > college_start:
        st.error(
            "⚠ Your morning routine doesn't fit before college starts."
        )
        return False

    return True


def validate_college_time(college_start, college_end):
    if college_end <= college_start:
        st.error(
            "⚠ College end time must be after college start time."
        )
        return False

    return True


def validate_wake_up_time(wake, college_start):
    if wake >= college_start:
        st.error(
            "⚠ Wake-up time must be before college starts."
        )
        return False

    return True
def validate_evening_schedule(study_start, college_end):
    if study_start < college_end:
        st.error(
            "⚠ Your evening activities don't fit after college. "
            "Reduce study, dinner, or relaxation time."
        )
        return False

    return True
