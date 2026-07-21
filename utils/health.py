import streamlit as st

def show_health_summary(home_study_hours, exercise, sleep_hours):
    st.subheader("📊 Health Summary")

    if home_study_hours < 2:
        st.warning("📚 Study at least 2 hours at home.")
    else:
        st.success("🎉 Great study schedule!")

    if exercise:
        st.success("✅ Great! Keep exercising.")
    else:
        st.info("💪 We've included a 30-minute exercise session.")

    st.success(f"😴 Recommended sleep: {sleep_hours} hours")