from src.rag_store import build_index

count = build_index("sample.pdf")

print(f"Indexed {count} chunks")