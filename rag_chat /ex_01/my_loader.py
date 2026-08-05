import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CURRENT_DIR.parents[1]  # 01-rag-chat

sys.path.insert(0, str(PROJECT_DIR))
from step_01_load_data import load_document

def main():
    file_path = PROJECT_DIR / "sample_data" / "intern_handbook.md"
    documents = load_document(str(file_path))
    total_characters = sum(len(doc.page_content) for doc in documents)

    print("=== Document Analysis ===")
    print(f"File: {file_path}")
    print(f"Total Documents: {len(documents)}")

    if documents:
        print("\nFirst 300 chars:")
        print(documents[0].page_content[:300])

        print("\nMetadata:")
        print(documents[0].metadata)

    print(f"\nTotal Characters: {total_characters}")

if __name__ == "__main__":
    main()