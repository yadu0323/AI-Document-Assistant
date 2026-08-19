import requests
from mcp_client import run_tool
from mcp_client import get_tools
# from tools.search_tool import search_document
# from tools.summary_tool import summarize_document
# from tools.keyword_tool import extract_keywords


OLLAMA_URL = "http://localhost:11434/api/generate"


def decide_tool(user_query):

    tools = get_tools()

    tool_names = [
        tool.name
        for tool in tools.tools
    ]

    prompt = f"""
You are an AI agent.

Available MCP tools:

ask_document
- Use for answering questions from the document.
- Examples:
  What is MySQL Workbench?
  What is a DBMS?
  How do I install MySQL?

document_summary
- Use when the user asks for a summary.
- Examples:
  Summarize this document.
  Give me a short summary.

document_keywords
- Use when the user asks for topics or keywords.
- Examples:
  What are the main topics?
  Extract keywords.

document_search
- Use ONLY when raw document passages are needed.
- Do NOT use for answering questions.

Return ONLY the tool name.

User Query:
{user_query}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen2.5-coder:7b",
            "prompt": prompt,
            "stream": False
        }
    )
    print(response.status_code)
    print(response.text)
    return response.json()["response"].strip()


def execute_tool(tool_name, query):

    if tool_name == "ask_document":

        return run_tool(
            "ask_document",
            {
                "question": query
            }
        )

    elif tool_name == "document_search":

        return run_tool(
            "document_search",
            {
                "query": query
            }
        )

    elif tool_name == "document_summary":

        return run_tool(
            "document_summary",
            {}
        )

    elif tool_name == "document_keywords":

        return run_tool(
            "document_keywords",
            {}
        )

    return "Unknown Tool"


def generate_final_answer(user_query, tool_result):

    prompt = f"""
You are an intelligent document assistant.

User Question:
{user_query}

Tool Output:
{tool_result}

Provide a helpful natural language answer.
Do not mention tools.
Do not mention MCP.
Answer directly.
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