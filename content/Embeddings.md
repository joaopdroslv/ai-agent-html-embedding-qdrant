## Embeddings

What are they?

An **embedding** is a **vetorized numerical representation** of some raw data - most commonly text, but also **images, audio**, etc. The goal of embeddings is to place semantically similar data close together in **high-dimensional space**,.

Example:

```bash
pip install sentence-transformers
```

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6v2")
embedding = model.encode("I love pizza!")
print(embedding.shape)  # e.g., (384,)
```

Analogy:

Imagine placing every word, sentence, or image in a giant 384D space. "Cat" and "Feline" are close. "Car" is far away. Embeddings make this possible.

Key Notes:

- Always of fixed size per model (e.g., 384, 512, 768 dimensions)
- Generated by AI models libe BERT, CLIP, etc.
- Input: unstructured data -> Output: list of `float32` numbers
