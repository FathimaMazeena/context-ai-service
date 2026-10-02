from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse
from app.rag.pipeline import RAGPipeline


router = APIRouter(
    prefix="/api/v1/chat",
    tags=["Chat"]
)


rag_pipeline = RAGPipeline()


@router.post(
    "",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest
) -> ChatResponse:

    result = rag_pipeline.ask(
        question=request.message
    )

    return ChatResponse(
        answer=result.answer,
        sources=result.sources
    )