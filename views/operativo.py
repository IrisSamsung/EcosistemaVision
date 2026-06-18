import streamlit as st

def show():
    st.components.v1.iframe(
     "https://app.powerbi.com/view?r=eyJrIjoiMGZlNTJiNjQtMDlhMi00MTRlLWE2YjktOTUzMTUwZmJkMzI4IiwidCI6ImQyYmMyMDhlLTRmZmYtNDA3OC1iNWFjLWY2OWE2YTI2NmZmMyIsImMiOjR9",
    height=800
        )