from fastapi import FastAPI

app = FastAPI(title="My RAG API")

@app.get("/")
def home():
    return {"status": "RAG Project is Running!"}

@app.get("/ask")
def ask(q: str):
    # এখানে তোমার Rag_analysis_pynb.ipynb এর logic পরে বসবে
    return {"question": q, "answer": "RAG থেকে উত্তর আসবে"}
