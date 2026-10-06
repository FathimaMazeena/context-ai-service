from app.rag.pipeline import RAGPipeline


def main():

    pipeline = RAGPipeline()

    # question = (
    #     "How long does delivery take "
    #     "outside Colombo?"
    # )

    question = (
        "Do you ship products internationally?"
    )

    response = pipeline.ask(
        question=question,
        n_results=3
    )

    print(f"\nQuestion:\n{question}")

    print("\n--- Answer ---")

    print(response.answer)

    print("\n--- Sources ---")

    for source in response.sources:
        print(
            f"- {source.id} | "
            f"{source.document_type} | "
            f"{source.source}"
        )


if __name__ == "__main__":
    main()