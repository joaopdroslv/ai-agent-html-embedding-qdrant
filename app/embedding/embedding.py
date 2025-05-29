import io

from docling.document_converter import DocumentConverter
from docling_core.types.io import DocumentStream
from langchain_community.embeddings import HuggingFaceEmbeddings
from qdrant_client.http.models import Distance, PointStruct, VectorParams

from app.db import COLLECTION_NAME, qdrant_client
from app.schemas.request_embedding import RequestEmbedding


def convert_html_to_markdown(html_content: str):
    html_bytes = html_content.encode("utf-8")

    document_stream = DocumentStream(
        name="temp_document.html", stream=io.BytesIO(html_bytes)
    )

    converter = DocumentConverter()

    result = converter.convert(document_stream)

    markdown_content = result.document.export_to_markdown()

    return markdown_content


def generate_embedding(request: RequestEmbedding):
    print(f"[INFO] Generating new embedding to: {request.title}")

    embeddings_model = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-large",
        model_kwargs={"device": "cpu", "trust_remote_code": True},
        encode_kwargs={"normalize_embeddings": True},
    )

    markdown_content = convert_html_to_markdown(request.body)

    print(f"[INFO] Generated markdown:\n\n {markdown_content}")

    embedded_body = embeddings_model.embed_query(markdown_content)

    return markdown_content, embedded_body


async def validate_qdrant_collection():
    collections = qdrant_client.get_collections().collections

    if not any(collection.name == COLLECTION_NAME for collection in collections):
        qdrant_client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
        )
        print("[INFO] Collection created.")
    else:
        print("[INFO] Collection already exists.")


# async def embedder(request: dict):
async def embedder(request_embedding: RequestEmbedding):
    await validate_qdrant_collection()

    # request_embedding = RequestEmbedding(**request)

    markdown_content, embedded_body = generate_embedding(request_embedding)

    request_embedding_dict = request_embedding.model_dump()
    request_embedding_dict["embeddings"] = embedded_body
    request_embedding_dict["body"] = markdown_content

    operation_info = qdrant_client.upsert(
        collection_name=COLLECTION_NAME,
        wait=True,
        points=[
            PointStruct(
                id=request_embedding.id,
                vector=embedded_body,
                payload=request_embedding_dict,
            )
        ],
    )

    print(f"[INFO] Operation info:\n\n {operation_info}")


def generate_embedding_text(text: str):
    embeddings_model = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-large",
        model_kwargs={"device": "cpu", "trust_remote_code": True},
        encode_kwargs={"normalize_embeddings": True},
    )

    return embeddings_model.embed_query(text)
