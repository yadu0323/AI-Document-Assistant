import streamlit as st
import os

from src.rag_store import build_index

from agent import (
    decide_tool,
    execute_tool,
    generate_final_answer
)

# -------------------------
# Chat History
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# PDF Upload
# -------------------------

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    save_path = os.path.join(
        "datas/uploads",
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    build_index(save_path)

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

# -------------------------
# UI
# -------------------------

st.title("📄 Document Assistant")

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Show old messages

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input

query = st.chat_input(
    "Ask a question"
)

# Process question

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.write(query)

    with st.spinner("Thinking..."):

        tool = decide_tool(query)

        tool_result = execute_tool(
            tool,
            query
        )

        answer = generate_final_answer(
            query,
            tool_result
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()