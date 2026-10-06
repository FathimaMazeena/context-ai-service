import json
from pathlib import Path

from app.rag.retrieval import RetrievalService


EVALUATION_FILE = Path(
    "evaluation/test_questions.json"
)


def load_evaluation_questions() -> list[dict]:
    with open(
        EVALUATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


def evaluate_retrieval(
    n_results: int = 3
) -> None:
    retrieval_service = RetrievalService()

    questions = load_evaluation_questions()

    answerable_questions = [
        question
        for question in questions
        if question["expected_source"] is not None
    ]

    top_1_correct = 0
    top_3_correct = 0

    for item in answerable_questions:
        retrieved_documents = (
            retrieval_service.retrieve(
                query=item["question"],
                n_results=n_results
            )
        )

        retrieved_ids = [
            document.id
            for document in retrieved_documents
        ]

        expected_source = item["expected_source"]

        if (
            retrieved_ids
            and retrieved_ids[0] == expected_source
        ):
            top_1_correct += 1

        if expected_source in retrieved_ids:
            top_3_correct += 1

        print(
            f"\n{item['id']}: "
            f"{item['question']}"
        )

        print(
            f"Expected: {expected_source}"
        )

        print(
            f"Retrieved: {retrieved_ids}"
        )

    total = len(answerable_questions)

    top_1_accuracy = (
        top_1_correct / total
        if total
        else 0
    )

    hit_at_3 = (
        top_3_correct / total
        if total
        else 0
    )

    print("\n--- Evaluation Results ---")

    print(
        f"Top-1 Accuracy: "
        f"{top_1_accuracy:.2%}"
    )

    print(
        f"Hit@3: "
        f"{hit_at_3:.2%}"
    )


if __name__ == "__main__":
    evaluate_retrieval()