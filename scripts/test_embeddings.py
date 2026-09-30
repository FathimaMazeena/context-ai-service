from app.rag.embeddings import EmbeddingService


def main():

    embedding_service = EmbeddingService()

    text = (
        "Wireless headphones with "
        "active noise cancellation."
    )

    embedding = embedding_service.embed_text(text)

    print(f"Text: {text}")
    print(f"Vector dimensions: {len(embedding)}")
    print(f"First 10 values: {embedding[:10]}")


if __name__ == "__main__":
    main()