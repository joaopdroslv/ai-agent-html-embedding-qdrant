from typing import List

from app.db import COLLECTION_NAME, qdrant_client
from app.schemas.category import Category
from app.schemas.user_level import UserLevel
from app.schemas.article import ArticleBase, Article


def get_all_embeddings_as_dicts() -> List[dict]:
    """Fetches all embeddings stored in Qdrant and returns them as dictionaries."""

    all_points, _ = qdrant_client.scroll(
        collection_name=COLLECTION_NAME,
        limit=100,
        with_vectors=True,
        with_payload=True,
    )
    embeddings = []
    for point in all_points:
        embeddings.append(
            {
                "id": point.id,
                "vector": point.vector,
                "payload": point.payload,
            }
        )
    return embeddings


def get_all_embeddings_articles() -> List[ArticleBase]:
    """Fetches the articles of all embeddings stored in Qdrant."""

    all_points, _ = qdrant_client.scroll(
        collection_name=COLLECTION_NAME, with_vectors=False, with_payload=True
    )
    articles = [ArticleBase(id=point.id, title=point.payload["title"]) for point in all_points]
    return articles


def get_all_embeddings_categories() -> List[Category]:
    """Fetches all unique categories from the embeddings stored in Qdrant."""

    all_points, _ = qdrant_client.scroll(
        collection_name=COLLECTION_NAME, with_vectors=False, with_payload=True
    )

    seen_ids = set()
    unique_categories = []

    for point in all_points:
        category_dicts = point.payload.get("categories", [])

        for category in category_dicts:
            if category["id"] not in seen_ids:
                seen_ids.add(category["id"])
                unique_categories.append(Category(**category))

    return unique_categories


def get_all_embeddings_levels() -> List[UserLevel]:
    """Fetches all unique user levels from the embeddings stored in Qdrant."""

    all_points, _ = qdrant_client.scroll(
        collection_name=COLLECTION_NAME, with_vectors=False, with_payload=True
    )

    seen_ids = set()
    unique_levels = []

    for point in all_points:
        level_dicts = point.payload.get("levels", [])

        for level in level_dicts:
            if level["id"] not in seen_ids:
                seen_ids.add(level["id"])
                unique_levels.append(UserLevel(**level))

    return unique_levels
