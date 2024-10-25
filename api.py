from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from PyPDF2 import PdfReader

app = FastAPI()
model = pipeline("question-answering", model="deepset/roberta-base-squad2")

class Query(BaseModel):
    question: str
    pdf_text: str

@app.post("/ask/")
def ask_question(query: Query):
    result = model(question=query.question, context=query.pdf_text)
    return {"answer": result['answer']}