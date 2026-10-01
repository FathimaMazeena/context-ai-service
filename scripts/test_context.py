from app.rag.context import build_context
from app.rag.retrieval import RetrievalService


def main():

    query = (
        "How long does delivery take "
        "outside Colombo?"
    )

    retrieval_service = RetrievalService()

    documents = retrieval_service.retrieve(
        query=query,
        n_results=3
    )

    context = build_context(documents)

    print(f"\nQuestion:\n{query}")

    print("\n--- RAG Context ---")

    print(context)


if __name__ == "__main__":
    main()