from qdrant_client.http.models import Distance, PointStruct, VectorParams

from app.db import COLLECTION_NAME, qdrant_client


async def validate_qdrant_collection(collection_name: str) -> None:
    """Checks if a Qdrant collection exists; creates it if it doesn't."""

    collections = qdrant_client.get_collections().collections

    if not any(collection.name == collection_name for collection in collections):
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
        )
        print("\n\n[INFO] Collection created.")

    else:
        print("\n\n[INFO] Collection already exists.")
