from pydantic_ai import RunContext  # Not context needed for now
from qdrant_client.http.models import (  # No filter needed for now
    FieldCondition,
    Filter,
    MatchValue,
)

from app.db import COLLECTION_NAME, qdrant_client
from app.embedding.embedding import generate_embedding_text
from app.schemas.rag_context import RagContext


async def retrieve_rag_context(question: str) -> RagContext:
    """
    Retrieves relevant context for a given question using semantic search on a Qdrant vector database.

    This function takes a user-provided question, generates its embedding, and performs a vector similarity
    search against a Qdrant collection. If similar content is found above the defined score threshold,
    the function extracts relevant topic IDs, titles, and content to build a RagContext object.
    """

    print(f"\n\n[INFO] User question:\n\n {question}")

    question_embedded = generate_embedding_text(question)

    search_result = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=question_embedded,
        # query_filter=Filter(should=[])  # No filter needed for now
        limit=10,
        score_threshold=0.85,
    )

    print(f"\n\n[INFO] Qdrant search results:\n\n {search_result}")

    if not search_result:
        result = RagContext(
            has_results=False,
            list_of_topics_ids=[],
            list_of_topics_titles=[],
            formatted_contents=[],
            message="No related information found.",
        )

        print(f"\n\n[INFO] Retrieved rag context:\n\n {result}")

        return result

    topics = []
    topics_titles = []
    formatted_contents = []

    for item in search_result:

        # Has item payload, item.payload is not null and payload has body
        if hasattr(item, "payload") and item.payload and "body" in item.payload:
            topics.append(item.id)  # Related topic ID
            topics_titles.append(item.payload["title"])  # Related topic title
            formatted_contents.append(item.payload["body"])  # Related topic content

    result = RagContext(
        has_results=len(topics) > 0,
        list_of_topics_ids=topics,
        list_of_topics_titles=topics_titles,
        formatted_contents=formatted_contents,
        message="Related information found.",
    )

    print(f"\n\n[INFO] Retrieved rag context:\n\n {result}")

    return result


if __name__ == "__main__":
    import asyncio

    result = asyncio.run(retrieve_rag_context("Why does the chameleon change color?"))
