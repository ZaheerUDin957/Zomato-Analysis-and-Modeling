import streamlit as st
from Introduction import Introduction
from Exploration import Exploration
from Reporting import Reporting
from Modeling import Modeling

st.set_page_config(page_title="Zomato", layout="wide")
st.title("Zomato Data Analysis and Modeling")

# Initialize session state for page navigation with "openai" as the default
if "page" not in st.session_state:
    st.session_state.page = "Introduction"

def navigate_to(page):
    st.session_state.page = page

# Create columns for navigation buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Introduction"):
        navigate_to("Introduction")

with col2:
    if st.button("Exploration"):
        navigate_to("Exploration")

with col3:
    if st.button("Reporting"):
        navigate_to("Reporting")

with col4:
    if st.button("Modeling"):
        navigate_to("Modeling")


# Display the appropriate page based on session state
if st.session_state.page == "Introduction":
    Introduction()
elif st.session_state.page == "Exploration":
    Exploration()
elif st.session_state.page == "Reporting":
    Reporting()
elif st.session_state.page == "Modeling":
    Modeling()
else:
    Introduction()  
