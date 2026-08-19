import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_llm(context, question):
    prompt = f"""
You are a helpful document assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen2.5-coder:7b",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]