import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CURRENT_DIR.parents[1]
sys.path.insert(0, str(PROJECT_DIR))

from step_01_load_data import load_document
SUPPORTED_EXTENSIONS = [".md", ".txt", ".pdf"]

def main():
    sample_folder = PROJECT_DIR / "sample_data"
    print("\n=== Sample Data Summary ===\n")
    print(f"{'Filename':<35}{'Documents':<12}{'Characters':<12}{'Type'}")
    print("-" * 75)

    for file in sorted(sample_folder.iterdir()):
        if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS:
            try:
                docs = load_document(str(file), verbose=False)

                total_chars = sum(len(doc.page_content) for doc in docs)

                print(
                    f"{file.name:<35}"
                    f"{len(docs):<12}"
                    f"{total_chars:<12}"
                    f"{file.suffix}"
                )
            except Exception as e:
                print(f"{file.name:<35}ERROR: {e}")

if __name__ == "__main__":
    main()