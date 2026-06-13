import os
import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.set_page_config(page_title="AI Research Paper Assistant")
st.title("📄 AI Research Paper Assistant")


uploaded_file = st.file_uploader(
    "Upload a Research Paper (PDF)",
    type=["pdf"]
)
text = ""

if uploaded_file is not None:

    st.success("PDF Uploaded Successfully!")

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    st.subheader("Extracted Text")

    st.text_area(
        "PDF Content",
        text,
        height=300
    )
if text:

    if st.button("Generate Summary"):

        with st.spinner("Analyzing paper..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""
Analyze the uploaded document and provide:

1. Short Summary
2. Key Skills
3. Important Technologies
4. Main Highlights
5. Final Conclusion

Document:

{text}
"""
            )

            summary = response.text

            st.subheader("AI Summary")
            st.write(summary)   