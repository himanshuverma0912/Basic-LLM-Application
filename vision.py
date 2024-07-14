# # Import necessary libraries:
# from dotenv import load_dotenv  # For loading environment variables from a .env file
# load_dotenv()  # Load environment variables (e.g., API keys)

# import streamlit as st  # For building the web app interface
# import os  # For interacting with the operating system (to get API key)
# import google.generativeai as genai  # Google's Gemini API library
# from PIL import Image
# # Configure the Gemini API:
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Set your Gemini API key from the environment

# # Define a function to interact with the Gemini model:
# model = genai.GenerativeModel("gemini-pro-vision")  # Create a Gemini model instance
# def get_gemini_response(input,image):  # Function to get a response from Gemini
#     if input !="":
#         response=model.generate_content([input,image])
#     else:
#         response = model.generate_content(image)  # Generate content based on the input question

#     return response.text

# # Set up the Streamlit app interface:
# st.set_page_config(page_title="Gemini Image Demo")  # Set the page title
# st.header("Gemini LLM Application")  # Display a header
# input = st.text_input("Input Prompt: ", key="input")  # Create a text input box for the question

# uploaded_file=st.file_uploader("Choose an Image...",type=["jpg","jpeg","png"])
# image=""
# if uploaded_file is not None:
#     image=Image.open(uploaded_file)
#     st.image(image,caption="Uploaded Image.",use_column_width=True)


# submit = st.button("Tell me about the image")  # Create a button to submit the question

# # if submit is clicked
# if submit:
#     response=get_gemini_response(input,image)
#     st.subheader("The Response is")
#     st.write(response)


# --- Load Environment Variables and Import Libraries ---

# Load environment variables from a '.env' file (e.g., your API key)
from dotenv import load_dotenv
load_dotenv()

# Streamlit for creating the web app interface
import streamlit as st
# Operating system interaction (e.g., to access environment variables)
import os
# Google's Gemini API for interacting with their generative AI model
import google.generativeai as genai
# Python Imaging Library (PIL) for handling images
from PIL import Image


# --- Set Up the Streamlit App's Page ---

# Configure the title that appears in the browser tab
st.set_page_config(page_title="Gemini Image Demo")

# --- Define Custom Styles for the Webpage ---
st.markdown("""
<style>
/* General Body Styles: Light gray background, standard sans-serif font */
body {
    background-color: #f4f4f4;
    font-family: Arial, sans-serif;
}

/* Main App Container: 
   - Sets max width, centers the content, adds padding,
     white background, rounded corners, and a subtle shadow */
.stApp {
    max-width: 900px;
    margin: auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Heading Styles: Dark gray text, centered alignment */
h1, h2 {
    color: #333;
    text-align: center;
}

/* Text Input Styles: Basic padding, border, and rounded corners */
.text-input {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 100%; 
}

/* Submit Button Styles: Green background, white text, various properties for look and feel */
.submit-button {
    background-color: #4CAF50; 
    border: none;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    border-radius: 4px;
    cursor: pointer; /* Indicate it's clickable */
    transition: background-color 0.3s; /* Smooth color change on hover */
}

/* Button Hover Effect: Slightly darker green on mouse hover */
.submit-button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)  # Allow raw HTML for styling



# --- Configure Gemini API Access ---

# Set up Gemini to use your API key from the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Create an instance of the Gemini Pro Vision model
model = genai.GenerativeModel("gemini-pro-vision")

# --- Function to Interact with Gemini ---

# Define a function to send input (text and/or image) to Gemini and get a response
def get_gemini_response(input, image):
    # If there's text input, send both text and image
    if input != "":
        response = model.generate_content([input, image])
    # If there's no text input, just send the image
    else:
        response = model.generate_content(image)
    # Return the text content of Gemini's response
    return response.text


# --- Build the Streamlit User Interface ---

# Display the main app heading
st.header("Gemini LLM Application")

# Create a text input box for the user to type a prompt
input = st.text_input("Input Prompt: ", key="input")

# Create a file uploader widget for images (jpg, jpeg, png)
uploaded_file = st.file_uploader("Choose an Image...", type=["jpg", "jpeg", "png"])
image = ""  # Initialize image variable
# If the user uploads a file
if uploaded_file is not None:
    # Open the image using PIL
    image = Image.open(uploaded_file)
    # Display the uploaded image in the app
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Create a button labeled "Tell me about the image"
submit = st.button("Tell me about the image")

# --- Process the User's Request ---

# If the button is clicked
if submit:
    # Show a "Processing..." message with custom styling while waiting for Gemini
    st.markdown('<p class="submit-button">Processing...</p>', unsafe_allow_html=True)  
    # Get a response from Gemini based on the input and image
    response = get_gemini_response(input, image)
    # Display a subheader indicating the start of the response
    st.subheader("The Response is")
    # Display the response text from Gemini
    st.write(response)
