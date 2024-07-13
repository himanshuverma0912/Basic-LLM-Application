# Import necessary libraries:
from dotenv import load_dotenv  # For loading environment variables from a .env file
load_dotenv()  # Load environment variables (e.g., API keys)

import streamlit as st  # For building the web app interface
import os  # For interacting with the operating system (to get API key)
import google.generativeai as genai  # Google's Gemini API library

# Configure the Gemini API:
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Set your Gemini API key from the environment

# Define a function to interact with the Gemini model:
model = genai.GenerativeModel("gemini-pro")  # Create a Gemini model instance
def get_gemini_response(question):  # Function to get a response from Gemini
    response = model.generate_content(question)  # Generate content based on the input question
    return response.text  # Return the text content of the response

# Set up the Streamlit app interface:
st.set_page_config(page_title="Q&A Demo")  # Set the page title
st.header("Gemini LLM Application")  # Display a header
input = st.text_input("Input: ", key="input")  # Create a text input box for the question
submit = st.button("Ask the question")  # Create a button to submit the question

# Handle button click:
if submit:  # If the "Ask the question" button is clicked
    response = get_gemini_response(input)  # Get the response from the Gemini model
    st.subheader("The Response is")  # Display a subheader for the response
    st.write(response)  # Display the Gemini model's response in the app




