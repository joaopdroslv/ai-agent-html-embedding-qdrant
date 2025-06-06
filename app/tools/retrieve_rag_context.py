from pydantic_ai import RunContext
from qdrant_client.http.models import FieldCondition, Filter, MatchValue

from app.db import COLLECTION_NAME, qdrant_client
from app.models.embedding_model import embeddings_model
from app.schemas.chat import LevelContext
from app.schemas.rag_context import RagContext, SimilarityScore


async def retrieve_rag_context(
    ctx: RunContext[LevelContext], question: str
) -> RagContext:
    """
    Retrieves relevant context for a given question using semantic search on a Qdrant vector database.

    This function takes a user-provided question, generates its embedding, and performs a vector similarity
    search against a Qdrant collection. If similar content is found above the defined score threshold,
    the function extracts relevant topic IDs, titles, and content to build a RagContext object.
    """

    print(f"\n\n[INFO] User question:\n\n {question}")
    print(f"\n\n[INFO] User level: {ctx.deps.level}")

    question_embedded = embeddings_model.embed_query(question)

    # print(f"\n\n[INFO] Embbeded question: {question_embedded}")

    search_result = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=question_embedded,
        query_filter=Filter(
            should=[
                FieldCondition(
                    key="levels[].id",
                    match=MatchValue(value=ctx.deps.level),
                ),
            ]
        ),
        limit=10,
        score_threshold=0.80,
    )

    print(f"\n\n[INFO] Qdrant search results:\n\n {search_result}")

    if not search_result:
        result = RagContext(
            has_results=False,
            list_of_topics_ids=[],
            list_of_topics_titles=[],
            formatted_contents=[],
            similarity_scores=[],
            message="No related information found.",
        )

        print(f"\n\n[INFO] Retrieved rag context:\n\n {result}")

        return result

    topics = []
    topics_titles = []
    formatted_contents = []
    similarity_scores = []

    for item in search_result:

        # Has item payload, item.payload is not null and payload has body
        if hasattr(item, "payload") and item.payload and "body" in item.payload:
            topics.append(item.id)  # Related topic ID
            topics_titles.append(item.payload["title"])  # Related topic title
            formatted_contents.append(item.payload["body"])  # Related topic content
            similarity_scores.append(
                SimilarityScore(
                    topic_id=item.id,
                    topic_title=item.payload["title"],
                    similarity_score=item.score,
                )
            )

    result = RagContext(
        has_results=len(topics) > 0,
        list_of_topics_ids=topics,
        list_of_topics_titles=topics_titles,
        formatted_contents=formatted_contents,
        similarity_scores=similarity_scores,
        message="Related information found.",
    )

    print(f"\n\n[INFO] Retrieved rag context:\n\n {result}")

    return result


if __name__ == "__main__":
    import asyncio

    result = asyncio.run(retrieve_rag_context("Why does the chameleon change color?"))
