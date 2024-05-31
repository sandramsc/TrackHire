from dotenv import load_dotenv

load_dotenv()

import streamlit as st

import base64
import os 
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configureapi_key=os.getenv("GOOGLE_API_KEY")

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
st.set_page_config(page_title = " TrackHire - ATS Resume Analyzer")
st.header("ATS Resume Analyzer")
input_text = st.text_area("Job Description: ", key= "input")
upload_file = st.file_uploader("Upload your resume in PDF format", type="pdf")

if upload_file is not None:
     st.write('PDF uploaded successfully')

submit_btn1 =st.button("Tell me about yourself?")
submit_btn2 =st.button("How can I improve my skills?")
submit_btn3 =st.button("Percentage match")
submit_btn4 = st.button("Identify top candidates")
submit_btn5 = st.button("Suggest resume improvements")
submit_btn6 = st.button("Summary of strengths and weaknesses")

# This is the prompt for the GENAI to act as an HR Tech Recruiter
input_prompt1 = """
You are an experienced HR professional specializing in data science, full-stack web development, and big data engineering. Use our advanced Tech HR LLM to analyze the provided resumes against the corresponding job descriptions. Ensure that candidate qualifications align precisely with the required skills and criteria for these roles.
"""


# This is the prompt for the GENAI to act as an ATS System
input_prompt2 = """
You are a proficient Tech HR specialist adept in arts, DevOps, and related fields. Use our Tech HR LLM to meticulously review resumes against the corresponding job descriptions. Ensure precise alignment between candidate qualifications and the required skill sets for optimal recruitment outcomes.
"""

# This is the prompt for the GENAI to provide a percentage match on the resume based on job description
input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. Evaluate the resume against the provided job description. Provide the percentage match if the resume aligns with the job description. Present the output as follows: 1) percentage match, 2) missing keywords, and 3) final thoughts.
"""

# This is the prompt for the GENAI to identify top candidates from a pool of resumes
input_prompt4 = """
You are an experienced Tech HR specialist with expertise in candidate selection for data science, full-stack web development, and big data engineering roles. Use our Tech HR LLM to identify the top candidates from a pool of resumes based on the provided job descriptions. Rank the candidates in order of best fit, highlighting their strengths and relevant qualifications.
"""

# This is the prompt for the GENAI to suggest improvements for a candidate's resume
input_prompt5 = """
You are a proficient resume analyst with expertise in optimizing resumes for data science, DevOps, and arts roles. Use our Tech HR LLM to review a candidate's resume and suggest specific improvements to enhance its alignment with a provided job description. Focus on optimizing keywords, skills, and overall presentation.
"""

# This is the prompt for the GENAI to provide a summary of candidate strengths and weaknesses
input_prompt6 = """
You are an experienced Tech HR analyst with a strong understanding of candidate evaluation. Use our Tech HR LLM to provide a summary of the strengths and weaknesses of a candidate based on their resume and the provided job description. Highlight key areas where the candidate excels and areas where they may need improvement.


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

if submit_btn3:
    if upload_file is not None:
          pdf_content= input_pdf_setup(upload_file)
          response = get_gemini_response(input_prompt3, pdf_content, input_text)
          st.subheader("The response is:")
          st.write(response)

if submit_btn4:
    if upload_file is not None:
          pdf_content= input_pdf_setup(upload_file)
          response = get_gemini_response(input_prompt4, pdf_content, input_text)
          st.subheader("The response is:")
          st.write(response)

if submit_btn5:
    if upload_file is not None:
          pdf_content= input_pdf_setup(upload_file)
          response = get_gemini_response(input_prompt5, pdf_content, input_text)
          st.subheader("The response is:")
          st.write(response)

if submit_btn6:
    if upload_file is not None:
          pdf_content= input_pdf_setup(upload_file)
          response = get_gemini_response(input_prompt6, pdf_content, input_text)
          st.subheader("The response is:")
          st.write(response)
