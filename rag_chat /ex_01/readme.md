Exercise 01: Custom Document Loader
Difficulty: ⭐ Beginner
Estimated Time: 30 minutes

🎯 Learning Objectives
Practice using LangChain document loaders
Understand document metadata
Learn to inspect loaded content
📝 Task
Create a Python script called my_loader.py that:

Loads a document of your choice from the sample_data/ folder (or create your own)
Prints the following information:
Total number of pages/documents loaded
The first 300 characters of content
All metadata fields
The total character count across all documents
✅ Success Criteria
Your script should output something like:

=== Document Analysis ===
File: sample_data/intern_handbook.md
Total Documents: 1
First 300 chars: [your content here]
Metadata: {'source': 'sample_data/intern_handbook.md'}
Total Characters: 1624
💡 Hints
Reuse the load_document() function from step_01_load_data.py
You can import it: from step_01_load_data import load_document
Use len(doc.page_content) to count characters
🚀 Bonus Challenge
Modify your script to load all files in sample_data/ and create a summary table showing:

Filename
Number of documents
Total characters
File type (.md, .txt, .pdf)
