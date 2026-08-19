from src.pdf_loader import extract_text_from_pdf
from src.chatbot import ask_llm

PDF_PATH = "sample.pdf"

def summarize_document():
    text = extract_text_from_pdf(PDF_PATH)

    short_text = text[:5000]

    prompt = """
Summarize this document in 5 concise bullet points.

Document:
""" + short_text

    return ask_llm(prompt, "")