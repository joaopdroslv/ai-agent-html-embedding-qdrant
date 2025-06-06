from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings_model = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-large",
    model_kwargs={"device": "cpu", "trust_remote_code": True},
    encode_kwargs={"normalize_embeddings": True},
)
