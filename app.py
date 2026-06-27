from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="EvalOps AI Platform",
    version="1.0.0"
)

class EvaluationRequest(BaseModel):
    question: str
    answer: str

@app.get("/")
def home():
    return {
        "status": "running",
        "project": "EvalOps AI Enterprise LLM Evaluation Platform"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/evaluate")
async def evaluate(req: EvaluationRequest):
    """
    Later you can integrate DeepEval metrics here.
    """
    return {
        "question": req.question,
        "answer": req.answer,
        "score": 1.0,
        "passed": True
    }
