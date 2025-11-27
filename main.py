from fastapi import FastAPI, HTTPException
import os
from pydantic import BaseModel
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

app = FastAPI()

DB_DIR = "chroma_db"

class QueryRequest(BaseModel):
    query: str

def get_rag_response(query: str) -> str:
    try:
        # 1. Load Vector Store
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vector_store = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
        
        # 2. Setup Retriever
        retriever = vector_store.as_retriever(search_kwargs={"k": 3})
        
        # 3. Setup LLM (Ollama)
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        llm = Ollama(
            base_url=base_url,
            model="llama3"
        )
        
        # 4. Create RAG Chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=False
        )
        
        # 5. Get Response
        response = qa_chain.invoke({"query": query})
        return response["result"]
        
    except Exception as e:
        return f"Error processing request: {str(e)}"

@app.post("/api/query")
async def query_endpoint(request: QueryRequest):
    response = get_rag_response(request.query)
    return {"response": response}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
