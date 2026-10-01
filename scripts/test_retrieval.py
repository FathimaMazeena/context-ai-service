from app.rag.retrieval import RetrievalService


def main():

    retrieval_service = RetrievalService()

    query = "What headphones can reduce background noise?"

    results = retrieval_service.retrieve(
        query=query,
        n_results=3
    )

    print(f"\nQuery: {query}")

    print("\n--- Retrieved Documents ---")

    for index, document in enumerate(results):

        print(f"\nRank: {index + 1}")
        print(f"Document ID: {document.id}")
        print(f"Distance: {document.distance}")
        print(f"Metadata: {document.metadata}")
        print(f"Content:\n{document.content}")
        print("-" * 50)


if __name__ == "__main__":
    main()