import streamlit as st


def show_employee_health_summary(exercise, sleep_hours):
    st.subheader("📊 Health Summary")

    # Exercise
    if exercise:
        st.success("✅ Great! Keep exercising regularly.")
    else:
        st.info("💪 We've included an exercise session in your timetable.")

    # Sleep
    if sleep_hours >= 8:
        st.success(f"😴 Excellent! You're getting {sleep_hours} hours of sleep.")
    else:
        st.warning(
            f"😴 You're getting {sleep_hours} hours of sleep. "
            "Try to aim for at least 8 hours when possible."
        )

    # Work-life balance reminder
    st.info("☕ Remember to take short breaks during work to stay productive.")

    # Hydration reminder
    st.info("💧 Stay hydrated throughout the day.")

    # Evening reminder
    st.info("🛋 Make time to relax before going to bed.")