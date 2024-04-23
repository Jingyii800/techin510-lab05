import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Function to get data from Gemini API
def get_data_from_gemini(requirements):
    response = model.generate_content(requirements)
    return response.text

# Streamlit interface
st.title('Travel Planner')

# Collect travel requirements from the user
col1, col2 = st.columns(2, gap="medium")
with col1:
    num = st.text_input("Enter the number of your group:")
    destination = st.text_input("Enter your destination:")
    budget = st.slider("Budget", 100, 5000, 1000)
with col2:
    start_date = st.date_input("Start date:")
    end_date = st.date_input("End date:")
    preference = st.text_input("Enter your interests: eg.museums, outdoor, indoor, love foods...")

requirements = f"Please make a plan for our trip. We have {num} and are going to {destination} from {start_date} to {end_date} and our budget is {budget}. Our interests are {preference}"

if st.button('Get Data'):
    data = get_data_from_gemini(requirements)
    st.write(data)
