import streamlit as st
from resume_parser import (
    extract_text,
    extract_email,
    extract_number,
    extract_name,
    extract_skills
)

# Page configuration
st.set_page_config(
    page_title="AI Resume Parser",
    layout="wide"
)

# Sidebar
st.sidebar.title("Resume Parser")
st.sidebar.write("NLP based Resume Analyzer")
st.sidebar.markdown("---")
st.sidebar.write("Name Extraction")
st.sidebar.write("Email Extraction")
st.sidebar.write("Phone Extraction")
st.sidebar.write("Skill Extraction")

# Main title
st.title("AI Resume Parser")
st.write("Upload a resume PDF and extract important information")

st.divider()

# File uploader
uploaded_file = st.file_uploader(
    "Upload Resume (PDF only)",
    type=["pdf"]
)

# Process resume
if uploaded_file is not None:
    with st.spinner("Analyzing resume..."):
        text = extract_text(uploaded_file)
        name = extract_name(text)
        email = extract_email(text)
        phone = extract_number(text)
        skills = extract_skills(text)

    st.success("Resume parsed successfully")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Candidate Details")
        st.info("Name: " + (name if name else "Not Found"))
        st.info("Email: " + (email if email else "Not Found"))
        st.info("Phone: " + (phone if phone else "Not Found"))

    with col2:
        st.subheader("Skills Extracted")
        if skills:
            for skill in skills:
                st.success(skill)
        else:
            st.warning("No skills found")

st.divider()
st.write("Resume Parser NLP Project using Streamlit")
