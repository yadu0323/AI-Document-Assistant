from mcp.server import MCPServer
from tools.wiki_tool import search_wikipedia
from tools.search_tool import search_document
from tools.summary_tool import summarize_document
from tools.keyword_tool import extract_keywords
from tools.qa_tool import document_qa

mcp = MCPServer("Document Assistant")

@mcp.tool()
def wiki_search(question: str) -> str:
    return search_wikipedia(question)

@mcp.tool()
def document_search(query: str) -> str:
    return search_document(query)


@mcp.tool()
def document_summary() -> str:
    return summarize_document()


@mcp.tool()
def document_keywords() -> str:
    return extract_keywords()


@mcp.tool()
def ask_document(question: str) -> str:
    return document_qa(question)


if __name__ == "__main__":
    mcp.run()