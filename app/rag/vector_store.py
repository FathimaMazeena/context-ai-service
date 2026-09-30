import chromadb

from app.core.config import settings
from app.models.document import KnowledgeDocument


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_PERSIST_DIR
        )

        self.collection = self.client.get_or_create_collection(
            name=settings.CHROMA_COLLECTION_NAME
        )

    def add_documents(
        self,
        documents: list[KnowledgeDocument],
        embeddings: list[list[float]]
    ) -> None:

        if len(documents) != len(embeddings):
            raise ValueError(
                "Number of documents and embeddings must match."
            )

        self.collection.upsert(
            ids=[
                document.id
                for document in documents
            ],

            documents=[
                document.content
                for document in documents
            ],

            embeddings=embeddings,

            metadatas=[
                {
                    **document.metadata,
                    "source": document.source,
                    "document_type": document.document_type
                }
                for document in documents
            ]
        )

    def query(
        self,
        query_embedding: list[float],
        n_results: int = 3
    ) -> dict:

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        return results    