import streamlit as st
from streamlit_option_menu import option_menu
selected =option_menu(menu_title="NLP",
                              options=["home","Contact","about"],
                              orientation="horizontal",)
if selected == "Contact":
    st.write="Name"
if selected == "about":
    st.write="Riya"
if selected == "home":
    st.write="ok"


