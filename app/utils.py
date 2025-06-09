from app.db import COLLECTION_NAME, qdrant_client


def get_unique_items_from_embeddings_payload(
    pydantic_model, payload_list_field, item_id_field
):
    """Extracts unique items from a list field of the payload of embeddings stored in Qdrant."""

    all_points, _ = qdrant_client.scroll(
        collection_name=COLLECTION_NAME, with_vectors=False, with_payload=True
    )

    seen_ids = set()
    unique_items = []

    for point in all_points:
        item_dicts = point.payload.get(payload_list_field, [])

        if not isinstance(item_dicts, list):
            print(f"[INFO]: The given payload field is not a list.")
            continue

        for item in item_dicts:
            if item[item_id_field] not in seen_ids:
                seen_ids.add(item[item_id_field])
                unique_items.append(pydantic_model(**item))

    return unique_items
