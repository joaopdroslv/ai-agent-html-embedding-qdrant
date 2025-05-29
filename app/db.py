from qdrant_client import QdrantClient

COLLECTION_NAME = "my_collection"

# Running inside docker
qdrant_client = QdrantClient(host="qdrant", port=6333)

# Running outside docker
# qdrant_client = QdrantClient(url="http://localhost:6333/", port=6333)
