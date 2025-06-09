from typing import List

from app.examples.request_embeddings import request_embeddings_examples
from app.modules.embedder import embed_n_insert_into_qdrant
from app.schemas.request_embedding import RequestEmbedding


async def disgest_documents(documents: List[RequestEmbedding]) -> None:
    """
    Processes and embeds a list of documents asynchronously.

    This function iterates over a list of embedding requests, logging the progress and attempting to generate
    embeddings for each using the `embedder` function. If an error occurs during embedding, it is caught
    and logged without interrupting the loop.
    """

    for document in documents:
        try:
            print(
                f'\n\n[INFO] Digesting document:\n\n\tID [ {document.id} ]\n\tTitle "{document.title}"'
            )
            await embed_n_insert_into_qdrant(document)
            print("\n\n[INFO] Document digested succesfully")

        except Exception as e:
            print(f'\n\n[ERROR] Error while Digesting: "{e}"')


if __name__ == "__main__":
    import asyncio

    asyncio.run(disgest_documents(request_embeddings_examples))
