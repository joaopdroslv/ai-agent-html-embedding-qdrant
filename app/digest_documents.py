from typing import List

from app.embedding.embedding import embedder
from app.examples.examples import request_embedding_examples
from app.schemas.request_embedding import RequestEmbedding


async def disgest_documents(documents: List[RequestEmbedding]):
    """
    Processes and embeds a list of documents asynchronously.

    This function iterates over a list of embedding requests, logging the progress and attempting to generate
    embeddings for each using the `embedder` function. If an error occurs during embedding, it is caught
    and logged without interrupting the loop.
    """

    for doc in documents:
        try:
            print(f'[INFO] Digesting document ID [ {doc.id} ] | Title "{doc.title}"')
            await embedder(doc)
            print("[INFO] Document digested succesfully")

        except Exception as e:
            print(f'[ERROR] Error while Digesting: "{e}"')


if __name__ == "__main__":
    import asyncio

    asyncio.run(disgest_documents(request_embedding_examples))
