from dotenv import load_dotenv
load_dotenv()  ##load all enviroment variable from .env file
import streamlit as st  ##frontend
import os  ## used for picking up enviroment variable assiging and from somewhere else
from PIL import Image
from pdf2image import convert_from_bytes
import google.generativeai as genai

# Secure access using Streamlit Secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

## Function to load Gemini 1.5 flash
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_respone(input, image, prompt):  ##input= how i want assistant to behave, image= what image we are going to pass, prompt=what i want out of image
    response = model.generate_content([input, image[0], prompt])  # in gemini flash they it takes parameters as list
    return response.text

def input_image_setup(uploaded_file):  # takes the uploaded file and give the all information in the bytes
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                "mime_type": uploaded_file.type,  ##Get the mine type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")

##intialize out streamlit app

st.set_page_config(page_title="MultiLanguage Invoice Extractor")

st.header("MultiLanguage Invoice Extractor")
st.caption("Created by Ashish Gossain") 
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg","jpeg","png","webp","pdf"])
image = None
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        try:
            images = convert_from_bytes(uploaded_file.read())
            image = images[0]  # Use the first page if multi-page
            st.image(image, caption="Uploaded PDF (Page 1)", use_container_width=True)
        except Exception as e:
            st.error(f"Error processing PDF: {e}")
    else:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
        except Exception as e:
            st.error(f"Error loading image: {e}")

submit = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in understanding invoices.
We will upload an image as invoices and you will have to answer any questions based on the uploaded invoice image"""

## If submit button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_respone(input_prompt, image_data, input)
    st.subheader("The Response is")
    st.write(response)