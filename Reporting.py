# Import necessary libraries
import pandas as pd
import seaborn as sns
from ydata_profiling import ProfileReport
import streamlit as st

# Load the dataset
df = pd.read_csv('zomato.csv', encoding='latin-1')

# Generate the profiling report
profile = ProfileReport(df, title='Zomato Dataset Profiling Report', explorative=True)

# Save the report as an HTML file
profile.to_file("Zomato.html")

# Streamlit application function
def Reporting():
    st.title('Zomato Report')
    # Display the report within the Streamlit app
    st.components.v1.html(profile.to_html(), height=800)

