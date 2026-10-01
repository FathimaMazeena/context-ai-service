from app.rag.generation import GenerationService


def main():

    question = (
        "How long does delivery take "
        "outside Colombo?"
    )

    # question = (
    #     "Do you deliver internationally?"
    # )



    context = """
[Source 1]
Document ID: shipping_policy_page_1
Type: policy
Content:
TechStore — Shipping Policy
Orders within Colombo are delivered within
2–3 working days.
Deliveries outside Colombo generally take
3–5 working days.
"""

    generation_service = GenerationService()

    answer = generation_service.generate(
        question=question,
        context=context
    )

    print(f"\nQuestion:\n{question}")

    print("\n--- Generated Answer ---")

    print(answer)


if __name__ == "__main__":
    main()