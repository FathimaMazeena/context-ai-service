
from app.models.document import KnowledgeDocument


def chunk_document(
    document: KnowledgeDocument,
    chunk_size: int = 700,
    chunk_overlap: int = 100
) -> list[KnowledgeDocument]:

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if chunk_overlap < 0 or chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be between 0 and chunk_size"
        )

    if document.document_type in ["product", "faq"]:
        return [document]

    text = document.content

    if len(text) <= chunk_size:
        return [document]

    chunks = []

    start = 0
    chunk_index = 0

    while start < len(text):

        end = min(start + chunk_size, len(text))

        chunk_text = text[start:end]

        chunk = KnowledgeDocument(
            id=f"{document.id}_chunk_{chunk_index}",
            content=chunk_text,
            source=document.source,
            document_type=document.document_type,
            metadata={
                **document.metadata,
                "parent_id": document.id,
                "chunk_index": chunk_index
            }
        )

        chunks.append(chunk)

        if end == len(text):
            break

        start = end - chunk_overlap
        chunk_index += 1

    return chunks
