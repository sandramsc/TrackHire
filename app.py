from dotenv import load_dotenv

load_dot_env()

import streamlit as st

import base64
import os 
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configureapi_key=os.getenv(("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generative_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(upload_file):
    if upload_file is not None:
        ## Convert PDF to image
        images = pdf2image.convert_from_bytes(upload_file.read.read())
        first_page = images[0]

        # Convert into bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file has been uploaded")


# Streamlit App
st.set_page_config(page_title = "ATS Resume Scanner")
st.header("ATS TRacking System")
input_text = st.text_area("Job DEscription: ", key= "input")
upload_file = st.file_uploader("Upload your resume in PDF format", type="pdf")

if upload_file is not None:
     st.write('PDF uploaded successfully')

submit_btn1 =st.button("Tell me about yourself?")

submit_btn2 =st.button("How can I improve my skills?")

submit_btn3 =st.button("Percentage match")

# THis is the prompt for the GENAI to act as  a HR Tech Recruiter
input_prompt1 = """
You are an experienced Tech HR specializing in data science, full-stack web development, and big data engineering. Utilize our advanced Tech HR LLM to review provided resumes against corresponding job descriptions for these roles. Ensure seamless alignment of candidate qualifications with specific skill sets and requirements.
"""

# THis is the prompt for the GENAI to act as  an ATS System
input_prompt2 = """

 a proficient Tech HR specialist adept in arts, devops, and related fields. Employ our Tech HR LLM to meticulously review resumes against corresponding job descriptions. Ensure seamless alignment between candidate qualifications and specific skill sets for optimal recruitment outcomes.
"""

if submit_btn1:
    if upload_file is not None:
          pdf_content= input_pdf_setup(upload_file)
          response = get_gemini_response(input_prompt1, pdf_content, input_text)
          st.subheader("The response is:")
          st.write(response)
    else:
        st.write("Please upload the resume")

elif submit_btn2:
    if upload_file is not None:
          pdf_content= input_pdf_setup(upload_file)
          response = get_gemini_response(input_prompt2, pdf_content, input_text)
          st.subheader("The response is:")
          st.write(response)
    else:
        st.write("Please upload the resume")