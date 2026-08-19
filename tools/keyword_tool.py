from src.pdf_loader import extract_text_from_pdf
from collections import Counter
import re

PDF_PATH = "sample.pdf"


def extract_keywords():
    text = extract_text_from_pdf(PDF_PATH)

    words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())

    common = Counter(words).most_common(20)

    return "\n".join(
        f"{word}: {count}"
        for word, count in common
    )