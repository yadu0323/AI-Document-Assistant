import faiss
import pickle
import numpy as np

from src.pdf_loader import extract_text_from_pdf
from src.chunker import chunk_text
from src.embeddings import create_embeddings, model
from src.vector_store import create_faiss_index, search


INDEX_FILE = "datas/faiss.index"
CHUNKS_FILE = "datas/chunks.pkl"


def build_index(pdf_path):
    text = extract_text_from_pdf(pdf_path)

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    index = create_faiss_index(embeddings)

    faiss.write_index(index, INDEX_FILE)

    with open(CHUNKS_FILE, "wb") as f:
        pickle.dump(chunks, f)

    return len(chunks)


def load_index():
    index = faiss.read_index(INDEX_FILE)

    with open(CHUNKS_FILE, "rb") as f:
        chunks = pickle.load(f)

    return index, chunks


def search_index(query, k=3):
    index, chunks = load_index()

    query_embedding = model.encode([query])[0]

    results = search(
        index,
        query_embedding,
        k
    )

    return "\n\n".join(
        chunks[i]
        for i in results
    )