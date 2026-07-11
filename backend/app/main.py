from fastapi import FastAPI

from app.routers.user_router import router as user_router

app = FastAPI(
    title="PatentVision-AI API"
)

app.include_router(user_router)


@app.get("/")
def root():
    return {
        "message": "PatentVision-AI Backend Running"
    }