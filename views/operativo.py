import streamlit as st

def show_malla():
    st.components.v1.iframe(
        "https://app.powerbi.com/view?r=eyJrIjoiMGZlNTJiNjQtMDlhMi00MTRlLWE2YjktOTUzMTUwZmJkMzI4IiwidCI6ImQyYmMyMDhlLTRmZmYtNDA3OC1iNWFjLWY2OWE2YTI2NmZmMyIsImMiOjR9",
        height=800
    )

def show_asistencia():
    st.components.v1.iframe(
        "https://app.powerbi.com/view?r=eyJrIjoiOGNhMDY5N2ItOGM2Zi00M2EzLThhMjctMWFmOTkyYjRiMTIyIiwidCI6ImQyYmMyMDhlLTRmZmYtNDA3OC1iNWFjLWY2OWE2YTI2NmZmMyIsImMiOjR9",
        height=800
    )

def show_seguimiento():
    st.components.v1.iframe(
        "https://app.powerbi.com/view?r=TU_LINK_SEGUIMIENTO",
        height=800
    )