import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic_ai import RunContext
from pydantic import ValidationError

from app.agents.answerer_agent import answerer_agent
from app.db import COLLECTION_NAME, qdrant_client
from app.schemas.chat import *
from app.tools.retrieve_rag_context import retrieve_rag_context
from app.schemas.answerer_agent_output import AnswererAgentOutput

router = APIRouter(prefix="/api/v1", tags=["chat"])


@router.get("/embeddings")
async def embeddings() -> JSONResponse:

    all_points = []

    scroll_result, _ = qdrant_client.scroll(
        collection_name=COLLECTION_NAME,
        limit=100,
        with_vectors=True,
    )

    all_points.extend(scroll_result)

    result = []
    for point in all_points:
        result.append(
            {
                "id": point.id,
                "vector": point.vector,
                "payload": point.payload,
            }
        )

    return JSONResponse(
        status_code=200,
        content={"code": 200, "message": "success", "embeddings": result},
    )


@router.post("/rag-retrieve")
async def rag_retrieve(request: ChatQuestion) -> JSONResponse:
    # Performs semantic search using Qdrant without involving an AI agent

    # Create a minimal context object, since retrieve_rag_context expects access to ctx.deps.level
    context = RunContext(
        model="",
        usage={},
        prompt=request.question,
        deps=LevelContext(level=request.level),
    )

    result = await retrieve_rag_context(context, request.question)

    return JSONResponse(
        status_code=200,
        content={
            "code": 200,
            "message": "success",
            "question": request.question,
            "result": result.model_dump(),
        },
    )


@router.post("/chat")
async def chat(request: ChatQuestion) -> JSONResponse:

    raw_result = await answerer_agent.run(
        request.question, deps=LevelContext(level=request.level)
    )

    if not hasattr(raw_result, "output"):
        raise HTTPException(status_code=500, detail="Agent did not return a valid output.")

    try:
        result_dict = json.loads(raw_result.output)
        result = AnswererAgentOutput(**result_dict)

    except (json.JSONDecodeError, ValidationError):
        raise HTTPException(
            status_code=500,
            detail="The agent returned an invalid or malformed JSON response."
        )

    except (json.JSONDecodeError, ValidationError):
        raise HTTPException(
            status_code=500,
            detail="The agent returned an invalid JSON response."
        )

    return JSONResponse(
        status_code=200,
        content={
            "code": 200,
            "message": "success",
            "question": request.question,
            "result": result.model_dump(),
        },
    )
