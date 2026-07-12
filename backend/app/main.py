from fastapi import FastAPI

from app.routers.user_router import router as user_router
from app.routers.project_router import router as project_router
from app.routers.image_router import router as image_router

app = FastAPI(
    title="PatentVision-AI API"
)
app.include_router(user_router)
app.include_router(project_router)
app.include_router(image_router)


@app.get("/")
def root():
    return {"message": "PatentVision-AI Backend Running"}