from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import base64
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import os

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text
    

def pdf_to_image(pdf_file):
    if pdf_file is not None:

        images = pdf2image.convert_from_bytes(pdf_file.read())
        page = images[0]

        images_byte_array = io.BytesIO()
        page.save(images_byte_array, format = "jpeg")
        images_byte_array = images_byte_array.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(images_byte_array).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file Uploaded")
    

## streamlit APP
st.set_page_config(page_title="ATS Resume Checker")
st.header("Gemini Pro Powered ATS Tracker")
st.subheader("Upload your resume and get a score on how well it will perform in an ATS")
job_description = st.text_area("Job Description:", key="input")
pdf_file = st.file_uploader("Upload your resume in PDF", type = ["pdf"])
if pdf_file is not None:
    st.write("PDF Uploaded Succesfully, Proceed to next step please")

prompt1 = st.button("Let Me know About the Resume")
prompt2 = st.button("What are things i Should do to improve my Skill")
prompt3 = st.button("ATS Score(Percentage Score)")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements. and be Precise with the Details
"""

input_prompt2 = """
You are an experienced Career Coach, I am interested in applying for a job, review the provided resume against the job description!
What specific skills and experiences should I focus on to improve my qualifications for this position? 
Could you provide a detailed plan that includes relevant courses, projects, certifications, and any other 
resources that will help me align my skills with the job requirements? Additionally, any tips on how to effectively
 demonstrate these skills during the application and interview process would be greatly appreciated.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if prompt1:
    if pdf_file is not None:
        pdf_images = pdf_to_image(pdf_file=pdf_file)
        response = get_gemini_response(input_prompt1, pdf_images, job_description)
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write("Please Upload your Resume")
    
if prompt2:
    if pdf_file is not None:
        pdf_images = pdf_to_image(pdf_file=pdf_file)
        response = get_gemini_response(input_prompt2, pdf_images, job_description)
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write("Please Upload your Resume")
    

if prompt3:
    if pdf_file is not None:
        pdf_images = pdf_to_image(pdf_file=pdf_file)
        response = get_gemini_response(input_prompt3, pdf_images, job_description)
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write("Please Upload your Resume")
    
