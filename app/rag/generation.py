from huggingface_hub import InferenceClient

from app.core.config import settings


class GenerationService:

    def __init__(self):

        if not settings.HF_TOKEN:
            raise ValueError(
                "HF_TOKEN is not configured."
            )

        self.client = InferenceClient(
            api_key=settings.HF_TOKEN
        )

    def generate(
        self,
        question: str,
        context: str
    ) -> str:

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful e-commerce "
                    "customer support assistant. "
                    "Answer the customer's question "
                    "using only the provided context. "
                    "Do not invent product details, "
                    "policies, prices, availability, "
                    "or other information. "
                    "If the context does not contain "
                    "enough information to answer the "
                    "question, say that you do not "
                    "have enough information."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Context:\n{context}\n\n"
                    f"Customer question:\n{question}"
                )
            }
        ]

        response = self.client.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=messages,
            max_tokens=300,
            temperature=0.2
        )

        answer = response.choices[0].message.content

        return answer.strip()