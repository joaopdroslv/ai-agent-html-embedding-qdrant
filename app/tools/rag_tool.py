from pydantic_ai import RunContext  # Not context needed for now
from qdrant_client.http.models import FieldCondition, Filter, MatchValue  # No filter needed for now

from app.db import COLLECTION_NAME, qdrant_client
from app.embedding.embedding import generate_embedding_text
from app.schemas.search_result import SearchResult


async def get_rag_data(question: str) -> SearchResult:
    print(f"\n\n[INFO] Question:\n\n {question}")

    question_embedded = generate_embedding_text(question)

    search_result = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=question_embedded,
        # query_filter=Filter(should=[])  # No filter needed for now
        limit=10,
        score_threshold=0.85,
    )

    print(f"\n\n[INFO] Search results:\n\n {search_result}")

    if not search_result:
        return SearchResult(
            has_results=False,
            list_of_topics_ids=[],
            list_of_topics_titles=[],
            formatted_contents=[],
            message="No related information found.",
        )

    topics = []
    topics_titles = []
    formatted_contents = []

    for item in search_result:

        # Has item payload, item.payload is not null and payload has body
        if hasattr(item, "payload") and item.payload and "body" in item.payload:
            topics.append(item.id)  # Related topic ID
            topics_titles.append(item.payload["title"])  # Related topic title
            formatted_contents.append(item.payload["body"])  # Related topic content

    result = SearchResult(
        has_results=len(topics) > 0,
        list_of_topics_ids=topics,
        list_of_topics_titles=topics_titles,
        formatted_contents=formatted_contents,
        message="Related information found.",
    )

    print(f"\n\n[INFO] Search result:\n\n {result}")

    return result


if __name__ == "__main__":
    import asyncio

    result = asyncio.run(get_rag_data("Why does the chameleon change color?"))
