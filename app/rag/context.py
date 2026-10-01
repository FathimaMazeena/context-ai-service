from app.models.retrieval import RetrievedDocument


def build_context(
    documents: list[RetrievedDocument]
) -> str:

    context_sections = []

    for index, document in enumerate(
        documents,
        start=1
    ):

        section = (
            f"[Source {index}]\n"
            f"Document ID: {document.id}\n"
            f"Type: "
            f"{document.metadata.get('document_type', 'unknown')}\n"
            f"Content:\n"
            f"{document.content}"
        )

        context_sections.append(section)

    return "\n\n".join(context_sections)