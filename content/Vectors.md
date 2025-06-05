## Vectors

What are they?

A **vector** in Qdrant is the actual list of numbers (i.e., the embedding) you store and search against.

```python
[0.213, -0.134, 0.900, ..., 0.001] # e.g., 512-dim vector
```

Notes:
- Every vector in a collection must have the **same dimensionality**
- Used as the main search target
