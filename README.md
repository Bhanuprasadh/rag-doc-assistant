# 📚 RAG Document Assistant

A local **Retrieval-Augmented Generation (RAG)** application that allows you to chat with your PDF documents using **Ollama (Llama 3)**, **FastAPI**, and **Streamlit**.

## 🚀 Features

*   **Chat with PDFs:** Upload documents and ask questions about them.
*   **Local Privacy:** Uses **Ollama** to run the LLM locally on your machine. No data leaves your computer.
*   **Vector Search:** Uses **ChromaDB** and **Sentence Transformers** for efficient document retrieval.
*   **Interactive UI:** Clean chat interface built with **Streamlit**.
*   **API First:** Backend powered by **FastAPI**.
*   **Containerized:** Docker support for easy deployment.
*   **Data Versioning:** DVC configured for managing documents and vector stores.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

1.  **Python 3.11+**
2.  **Docker** (optional, for containerized run)
3.  **Ollama**: [Download here](https://ollama.com)
4.  **Git**

---

## ⚡ Quick Start

### 1. Install & Setup Ollama
This project uses Llama 3 running locally.

1.  Download and install **Ollama** from [ollama.com](https://ollama.com).
2.  Open your terminal and pull the model:
    ```bash
    ollama pull llama3:8b
    ```
3.  Keep the Ollama app running in the background.

### 2. Clone the Repository
```bash
git clone https://github.com/Bhanuprasadh/rag-doc-assistant.git
cd rag-doc-assistant
```

### 3. Run with Docker (Recommended)
The easiest way to run the app is using Docker Compose.

```bash
docker-compose up --build
```
*   **Frontend:** Open [http://localhost:8501](http://localhost:8501)
*   **Backend API:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐍 Manual Installation (Python)

If you prefer running it without Docker:

1.  **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ingest Documents:**
    Place your PDF files in the `docs/` folder and run:
    ```bash
    python ingest.py
    ```

4.  **Start the Backend:**
    ```bash
    uvicorn main:app --reload
    ```

5.  **Start the Frontend (in a new terminal):**
    ```bash
    streamlit run app.py
    ```

---

## 📂 Project Structure

*   `main.py`: FastAPI backend handling the RAG logic and API endpoints.
*   `app.py`: Streamlit frontend for the chat interface.
*   `ingest.py`: Script to process PDFs and create the vector database.
*   `docs/`: Folder to store your PDF documents.
*   `chroma_db/`: Directory where the vector database is saved.
*   `Dockerfile` & `docker-compose.yml`: Configuration for containerization.

---

## 🔄 Data Version Control (DVC)

We use **DVC** to track the `docs/` folder and `chroma_db/` directory.

*   To add new documents:
    1.  Put files in `docs/`.
    2.  Run ingestion: `python ingest.py`
    3.  Track changes:
        ```bash
        dvc add docs chroma_db
        git add docs.dvc chroma_db.dvc
        git commit -m "Update documents"
        ```

---

## 🤝 Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements!
