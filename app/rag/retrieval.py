from app.models.retrieval import RetrievedDocument
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
    ) -> list[RetrievedDocument]:

        query_embedding = self.embedding_service.embed_text(
            query
        )

        results = self.vector_store.query(
            query_embedding=query_embedding,
            n_results=n_results
        )

        retrieved_documents = []

        ids = results["ids"][0]
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for index, document_id in enumerate(ids):

            retrieved_document = RetrievedDocument(
                id=document_id,
                content=documents[index],
                metadata=metadatas[index],
                distance=distances[index]
            )

            retrieved_documents.append(
                retrieved_document
            )

        return retrieved_documents