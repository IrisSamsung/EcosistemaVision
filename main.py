import streamlit as st
from views import comisiones, nhc, operativo, sample

st.set_page_config(page_title="ECOSISTEMA VISION", layout="wide")
st.title("📊 ECOSISTEMA VISION Y MARKETING")

tab1, tab2, tab3, tab4 = st.tabs([
    "💰 Comisiones",
    "👨🏽‍💻 NHC",
    "⚙️ Operativo",
    "🎯 Sample"
])

with tab1:
    comisiones.show()

with tab2:
    nhc.show()

with tab3:
    operativo.show()

with tab4:
    sample.show()