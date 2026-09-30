from app.rag.embeddings import EmbeddingService
from app.rag.vector_store import VectorStore


class RetrievalService:

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def retrieve(
        self,
        query: str,
        n_results: int = 3
    ) -> dict:

        query_embedding = self.embedding_service.embed_text(
            query
        )

        results = self.vector_store.query(
            query_embedding=query_embedding,
            n_results=n_results
        )

        return results