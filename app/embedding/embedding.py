import io
from typing import List, Tuple

from docling.document_converter import DocumentConverter
from docling_core.types.io import DocumentStream
from langchain_community.embeddings import HuggingFaceEmbeddings
from qdrant_client.http.models import Distance, PointStruct, VectorParams

from app.db import COLLECTION_NAME, qdrant_client
from app.schemas.request_embedding import RequestEmbedding


def convert_html_to_markdown(html_content: str) -> str:
    """Converts raw HTML content into Markdown using Docling."""

    # Convert the HTML content to bytes
    html_bytes = html_content.encode("utf-8")

    # Convert the bytes to a stream document, easier to docling process later,
    # docling will read the document stream as a html file,
    # even though it is just bytes in memory
    document_stream = DocumentStream(
        name="temp_document.html", stream=io.BytesIO(html_bytes)
    )

    converter = DocumentConverter()

    result = converter.convert(document_stream)

    markdown_content = result.document.export_to_markdown()

    return markdown_content


def generate_embedding(request: RequestEmbedding) -> Tuple[str, List[float]]:
    """Generates an embedding from HTML content after converting it to Markdown."""

    print(f"[INFO] Generating new embedding to: {request.title}")

    embeddings_model = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-large",
        model_kwargs={"device": "cpu", "trust_remote_code": True},
        encode_kwargs={"normalize_embeddings": True},
    )

    markdown_content = convert_html_to_markdown(request.body)

    # Lets concatenate the title with the body to facilitate the semantic search
    markdown_content = f"# {request.title}\n\n{markdown_content}"

    print(f"[INFO] Generated markdown:\n\n {markdown_content}")

    embedded_body = embeddings_model.embed_query(markdown_content)

    return markdown_content, embedded_body


async def validate_qdrant_collection(collection_name: str) -> None:
    """Checks if a Qdrant collection exists; creates it if it doesn't."""

    collections = qdrant_client.get_collections().collections

    if not any(collection.name == collection_name for collection in collections):
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
        )
        print("[INFO] Collection created.")

    else:
        print("[INFO] Collection already exists.")


async def embedder(request_embedding: RequestEmbedding) -> None:
    """Generates and stores the embedding of a given document into Qdrant."""

    await validate_qdrant_collection(COLLECTION_NAME)

    markdown_content, embedded_body = generate_embedding(request_embedding)

    request_embedding_dict = request_embedding.model_dump()
    request_embedding_dict["embeddings"] = embedded_body
    request_embedding_dict["body"] = markdown_content

    qdrant_upsert_result = qdrant_client.upsert(
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

    print(f"[INFO] Qdrant upsert result:\n\n {qdrant_upsert_result}")


def generate_embedding_text(text: str) -> List[float]:
    """Generates an embedding for a plain text input, such as a user question."""

    embeddings_model = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-large",
        model_kwargs={"device": "cpu", "trust_remote_code": True},
        encode_kwargs={"normalize_embeddings": True},
    )

    return embeddings_model.embed_query(text)
