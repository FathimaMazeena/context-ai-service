
import json
from pathlib import Path

import pymupdf

from app.models.document import KnowledgeDocument


def load_products(file_path: str) -> list[KnowledgeDocument]:

    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        products = json.load(file)

    documents = []

    for product in products:

        features = ", ".join(product.get("features", []))

        content = (
            f"Product: {product['name']}\n"
            f"Brand: {product['brand']}\n"
            f"Category: {product['category']}\n"
            f"Description: {product['description']}\n"
            f"Features: {features}\n"
            f"Warranty: {product.get('warranty', 'Not specified')}"
        )

        document = KnowledgeDocument(
            id=product["id"],
            content=content,
            source=path.name,
            document_type="product",
            metadata={
                "product_id": product["id"],
                "brand": product["brand"],
                "category": product["category"]
            }
        )

        documents.append(document)

    return documents


def load_faqs(file_path: str) -> list[KnowledgeDocument]:

    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        faqs = json.load(file)

    documents = []

    for faq in faqs:

        content = (
            f"Question: {faq['question']}\n"
            f"Answer: {faq['answer']}"
        )

        document = KnowledgeDocument(
            id=faq["id"],
            content=content,
            source=path.name,
            document_type="faq",
            metadata={
                "faq_id": faq["id"]
            }
        )

        documents.append(document)

    return documents


def load_pdf(file_path: str) -> list[KnowledgeDocument]:

    path = Path(file_path)

    documents = []

    with pymupdf.open(path) as pdf:

        for page_number, page in enumerate(pdf, start=1):

            content = page.get_text().strip()

            if not content:
                continue

            document = KnowledgeDocument(
                id=f"{path.stem}_page_{page_number}",
                content=content,
                source=path.name,
                document_type="policy",
                metadata={
                    "page": page_number,
                    "filename": path.name
                }
            )

            documents.append(document)

    return documents
