import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DOCS_DIR = "docs"
DB_DIR = "chroma_db"

def main():
    # 1. Load PDFs
    documents = []
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)
        print(f"Created {DOCS_DIR} directory. Please put your PDF files there.")
        return

    files = [f for f in os.listdir(DOCS_DIR) if f.endswith(".pdf")]
    if not files:
        print(f"No PDF files found in {DOCS_DIR}.")
        return

    print(f"Found {len(files)} PDF files. Loading...")
    for file in files:
        file_path = os.path.join(DOCS_DIR, file)
        loader = PyPDFLoader(file_path)
        documents.extend(loader.load())

    # 2. Split Text
    print("Splitting text...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    # 3. Generate Embeddings and Store in ChromaDB
    print("Generating embeddings and storing in ChromaDB...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Create and persist the vector store
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR
    )
    
    print(f"Ingestion complete. Vector store saved to {DB_DIR}")

if __name__ == "__main__":
    main()
