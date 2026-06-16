import streamlit as st

def show():
    st.components.v1.iframe(
     "https://app.powerbi.com/view?r=eyJrIjoiM2Q1ZTZmZjUtM2ZlZi00Yzg5LTk1ZWUtMGYyY2JlZWNkMDQxIiwidCI6ImQyYmMyMDhlLTRmZmYtNDA3OC1iNWFjLWY2OWE2YTI2NmZmMyIsImMiOjR9",
    height=800
        )