from fastapi import FastAPI

app = FastAPI(title="My RAG Project API")

@app.get("/")
def home():
    return {"message": "RAG API is Running!"}

@app.get("/ask")
def ask_question(q: str):
    # এখানে পরে তোমার RAG Logic বসবে
    return {"question": q, "answer": "This is from my RAG Analysis Notebook"}
