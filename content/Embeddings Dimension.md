# Embeddings Dimensions

## What Does "384D", "512D", etc. Mean?

These refer to the **number of dimensions** in the vector space - that is, the **length of the list of float numbers** that make up an embedding.

Example:

```python
vetor_384d = [0.123, -0.231, ..., 0.064]  # 384 float32 values
```

## What Does Each Dimension Represent?

Each dimension captures a **latent feature** learned by the model. These are not interpretable individually, but together, they capture the **semantic essence** of the input.

For example, in a sentence embedding:
- One dimension might loosely represent sentiment.
- Another might relate to topic.
- Another might capture tense or style.

The **model learns these features** during training, and higher dimensionality gives it **more "room" to represent complexity**.

## Why Use Larger Embeddings? (e.g., 768D, 1024D)

Benefits:

1. **Higher Expressive Power**
- More dimensions = more information captured.
- Ideal for complex inputs (long text, code, multimodal data).

2. **Improved Accuracy**
- Better semantic distinction between similar inputs.
- Less "overlap" in vector space.

3. **Better Performance on Downstream Tasks**
- For tasks like classification, ranking or retrieval, more dimensions often improve model accuracy - to a point.

## Downsides of Large Embeddings

Cons:

1. **Higher Storage Cost**
- Each vector uses more memory (e.g., 768D x 4 bytes = ~3KB per vector with float32).
- Millions of vectors add up quickly.

2. **Slower Indexing/Search**
- High-dimensional vectors are more computationally expensive for:
    - Distance calculations (cosine, dot product).
    - ANN (approximate nearest neighbor) structures like HNSW.

3. **Diminishing Returns**
- Beyond a certain size (e.g., > 1536D), you may not gain much accuracy.
- More dimensions != always better.
