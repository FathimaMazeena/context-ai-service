from app.rag.retrieval import RetrievalService


def main():

    retrieval_service = RetrievalService()

    #query = "What headphones can reduce background noise?"
    query = "How long does delivery take outside Colombo?"

    results = retrieval_service.retrieve(
        query=query,
        n_results=3
    )

    print(f"\nQuery: {query}")

    print("\n--- Retrieved Documents ---")

    ids = results["ids"][0]
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for index, document_id in enumerate(ids):

        print(f"\nRank: {index + 1}")
        print(f"Document ID: {document_id}")
        print(f"Distance: {distances[index]}")
        print(f"Metadata: {metadatas[index]}")
        print(f"Content:\n{documents[index]}")
        print("-" * 50)


if __name__ == "__main__":
    main()