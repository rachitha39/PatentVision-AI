from fastapi import FastAPI

app = FastAPI(
    title="PatentVision AI",
    version="1.0.0",
    description="AI-powered patent drawing generator"
)

@app.get("/")
def root():
    return {"message": "PatentVision AI Backend is Running 🚀"}

@app.get("/health")
def health():
    return {"status": "healthy"}