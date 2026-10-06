import json
from pathlib import Path

from app.rag.pipeline import RAGPipeline


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


def evaluate_generation() -> None:
    pipeline = RAGPipeline()

    questions = load_evaluation_questions()

    for item in questions:
        response = pipeline.ask(
            question=item["question"],
            n_results=3
        )

        print(
            f"\n{'=' * 60}\n"
            f"{item['id']}: {item['question']}"
        )

        print("\nGenerated Answer:")
        print(response.answer)

        print("\nExpected Facts:")
        if item["expected_facts"]:
            for fact in item["expected_facts"]:
                print(f"- {fact}")
        else:
            print("- None (unsupported question)")

        print("\nRetrieved Sources:")
        for source in response.sources:
            print(f"- {source.id}")

        print(
            f"\nExpected Answerable: "
            f"{item['answerable']}"
        )


if __name__ == "__main__":
    evaluate_generation()