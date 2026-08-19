from src.rag_store import search_index
from src.chatbot import ask_llm


def document_qa(question: str):

    context = search_index(question)

    answer = ask_llm(
        context,
        question
    )

    return answer