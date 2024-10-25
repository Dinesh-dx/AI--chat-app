import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline

st.title("AI Chat with PDF Knowledge Base")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")
if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    st.write("File uploaded successfully!")   
    model = pipeline("question-answering", model="deepset/roberta-base-squad2") 
    question = st.text_input("Ask a question based on the PDF")
    if question:
         if text.strip():  # Check if extracted text is not empty
            result = model(question=question, context=text)
            st.write("Answer:", result['answer'])
         else:
            st.write("No text found in the PDF. Please ensure the PDF contains extractable text.")
else:
    st.write("Please upload a PDF to get started.")
        