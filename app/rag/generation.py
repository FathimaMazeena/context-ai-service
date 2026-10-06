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
                    "You are a helpful e-commerce customer support assistant. "
                    "Answer the customer's question using only the provided context. "

                    "If the context contains information that answers the question, "
                    "answer using that information even when the information includes "
                    "conditions or limitations. Clearly include those conditions in "
                    "your answer. "

                    "Do not assume that a customer is asking whether something applies "
                    "universally unless they explicitly ask that. "

                    "For example, if the context says cash on delivery is available "
                    "for selected locations and the customer asks whether they can pay "
                    "when the order arrives, explain that cash on delivery is available "
                    "for selected locations. Do not reject the question simply because "
                    "the option is not available everywhere. "

                    "Do not invent product details, policies, prices, availability, "
                    "or other information. "

                    "If the context genuinely contains no information that answers "
                    "the customer's question, say that you do not have enough "
                    "information."

                    "Do not mention internal document IDs or source numbers in the answer."

                    "Do not suggest actions, contact methods, policies, "
                    "or next steps unless they are supported by the "
                    "provided context. "

                    
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