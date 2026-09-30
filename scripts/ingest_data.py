from pathlib import Path

from app.rag.loaders import (
    load_products,
    load_faqs,
    load_pdf
)

from app.rag.chunking import chunk_document
from app.rag.embeddings import EmbeddingService
from app.rag.vector_store import VectorStore


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def main():

    documents = []

    # Load products
    products = load_products(
        str(DATA_DIR / "products/sample_products.json")
    )

    documents.extend(products)

    # Load FAQs
    faqs = load_faqs(
        str(DATA_DIR / "faqs/sample_faqs.json")
    )

    documents.extend(faqs)

    # Load policy documents
    policy_dir = DATA_DIR / "policies"

    for pdf_file in sorted(policy_dir.glob("*.pdf")):

        policy_documents = load_pdf(str(pdf_file))

        documents.extend(policy_documents)

    # Process documents
    processed_documents = []

    for document in documents:

        chunks = chunk_document(document)

        processed_documents.extend(chunks)

    print(f"\nOriginal documents: {len(documents)}")
    print(f"Processed documents: {len(processed_documents)}")

    print("\n--- Processed Knowledge Base ---")

    for document in processed_documents:

        print(f"\nDocument ID: {document.id}")
        print(f"Type: {document.document_type}")
        print(f"Source: {document.source}")
        print(f"Content:\n{document.content[:200]}")
        print("-" * 50)

    # Generate embeddings
    print("\nGenerating embeddings...")

    embedding_service = EmbeddingService()

    texts = [
        document.content
        for document in processed_documents
    ]

    embeddings = embedding_service.embed_documents(texts)

    print(
        f"Generated {len(embeddings)} embeddings."
    )

    # Store documents and embeddings in ChromaDB
    vector_store = VectorStore()

    vector_store.add_documents(
        processed_documents,
        embeddings
    )

    print(
        f"Stored {len(processed_documents)} "
        "documents in ChromaDB."
    )

    return processed_documents


if __name__ == "__main__":
    main()