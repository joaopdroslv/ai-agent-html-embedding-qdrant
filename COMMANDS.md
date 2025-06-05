## Test Local Model Connection

Run this command to test the connection with the qwen/ollama model that is running locally.

```bash
docker exec -it chat-api python -m app.scripts.test_model_connection
```

## Digest Documents

Run this command to execute the `digest_documents` module, which processes documents `(e.g., from examples/request_embeddings.py)` and stores their embeddings into the Qdrant database.

```bash
docker exec -it chat-api python -m app.scripts.digest_documents
```
