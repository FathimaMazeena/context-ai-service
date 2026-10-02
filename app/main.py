
from fastapi import FastAPI

from app.core.config import settings
from app.api.health import router as health_router
from app.api.chat import router as chat_router


app = FastAPI(
    title=settings.APP_NAME,
    description=(
        "Standalone Retrieval-Augmented Generation "
        "service for e-commerce applications."
    ),
    version="1.0.0",
    debug=settings.DEBUG
)


app.include_router(
    health_router,
    prefix="/api/v1"
)

app.include_router(chat_router)


@app.get("/")
def root():

    return {
        "message": "E-Commerce RAG AI Service",
        "status": "running"
    }
