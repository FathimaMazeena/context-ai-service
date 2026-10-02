from fastapi.testclient import TestClient

from app.main import app
from app.models.rag import RAGResponse, RAGSource
from app.api import chat as chat_module


client = TestClient(app)


def test_chat_endpoint(monkeypatch):

    def mock_ask(
        question: str,
        n_results: int = 3
    ) -> RAGResponse:

        return RAGResponse(
            answer=(
                "Deliveries outside Colombo generally "
                "take 3–5 working days."
            ),
            sources=[
                RAGSource(
                    id="shipping_policy_page_1",
                    source="shipping_policy.pdf",
                    document_type="policy"
                )
            ]
        )

    monkeypatch.setattr(
        chat_module.rag_pipeline,
        "ask",
        mock_ask
    )

    response = client.post(
        "/api/v1/chat",
        json={
            "message": (
                "How long does delivery take "
                "outside Colombo?"
            )
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert (
        data["answer"]
        == "Deliveries outside Colombo generally "
           "take 3–5 working days."
    )

    assert data["sources"][0]["id"] == (
        "shipping_policy_page_1"
    )


def test_chat_rejects_empty_message():

    response = client.post(
        "/api/v1/chat",
        json={
            "message": ""
        }
    )

    assert response.status_code == 422