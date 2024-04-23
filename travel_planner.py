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
num = st.text_input("Enter the number of your group:")
destination = st.text_input("Enter your destination:")
start_date = st.date_input("Start date:")
end_date = st.date_input("End date:")
budget = st.slider("Budget", 100, 5000, 1000)
requirements = f"Please make a plan for our trip. We have {num} and are going to {destination} from {start_date} to {end_date} and our budget is {budget}."

if st.button('Get Data'):
    data = get_data_from_gemini(requirements)
    st.write(data)
