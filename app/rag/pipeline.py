from app.models.rag import RAGResponse, RAGSource
from app.rag.context import build_context
from app.rag.generation import GenerationService
from app.rag.retrieval import RetrievalService


class RAGPipeline:

    def __init__(self):

        self.retrieval_service = RetrievalService()
        self.generation_service = GenerationService()

    def ask(
        self,
        question: str,
        n_results: int = 3
    ) -> RAGResponse:

        # Step 1: Retrieve relevant documents
        documents = self.retrieval_service.retrieve(
            query=question,
            n_results=n_results
        )

        # Step 2: Build context for the LLM
        context = build_context(documents)

        # Step 3: Generate a grounded answer
        answer = self.generation_service.generate(
            question=question,
            context=context
        )

        # Step 4: Prepare source information
        sources = [
            RAGSource(
                id=document.id,
                source=document.metadata.get(
                    "source",
                    "unknown"
                ),
                document_type=document.metadata.get(
                    "document_type",
                    "unknown"
                )
            )
            for document in documents
        ]

        # Step 5: Return the complete RAG response
        return RAGResponse(
            answer=answer,
            sources=sources
        )