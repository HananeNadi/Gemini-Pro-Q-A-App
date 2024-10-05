from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Gemini Pro - Interactive Q&A Powered by AI")  
st.header("Gemini Pro Q&A: Ask Any Question, Get AI-Powered Responses")  
input = st.text_input('Enter your question:', key='input')  
submit = st.button("Ask the question") 

if submit:
    if input.strip() == "":  
        st.warning("Please enter a valid question before submitting!")  
    else:
        response = get_gemini_response(input)
        st.subheader("The response is:")
        st.write(response)
