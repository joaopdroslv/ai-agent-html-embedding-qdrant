## 🧠 AI Embedding & AI Agents Playground

This project is a learning and experimentation environment designed to explore and improve concepts related to **embeddings**, **vectorization**, and **AI agents**, with a focus on using **Pydantic AI** and **Qdrant** as a vector database.

The application is built using **FastAPI** and provides several endpoints to interact with embeddings, perform retrieval-augmented generation (RAG), and run agent-based responses.

### 🚀 Features

- Embedding generation and storage with Qdrant
- Retrieval of semantically similar documents (RAG)
- AI agent-based answers using Pydantic AI
- REST API built with FastAPI for interaction
- Schema validation with Pydantic

### 🧠 Project Goals

This repository serves as a personal lab for:
- Understanding how embeddings are generated, stored, and queried
- Building reliable and structured AI agents
- Experimenting with context-aware response systems (RAG)
- Gaining experience with vector DBs and prompt engineering

### 📌 Notes
- The project is still **under active development**.
- Only **basic error handling and validation** are in place.
- Ideal for **research, experimentation, and local use**.


## How to Run the Project

### 🛠️ Build and Start All Services

```bash
docker compose up --build -d
```

### 🤖 Test Local Model Connection

Run this command to test the connection with the qwen/ollama model that is running locally.

```bash
docker exec -it chat-api python -m app.scripts.test_model_connection
```

### 📄 Process and Store Document Embeddings

Run this command to execute the `digest_documents` module, which processes documents `(e.g., from examples/request_embeddings.py)` and stores their embeddings into the Qdrant database.

```bash
docker exec -it chat-api python -m app.scripts.digest_documents
```

### 📊 Access the Qdrant Dashboard

You can view and manage your Qdrant collections via

```
http://localhost:6333/dashboard
```
