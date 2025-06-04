from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic_ai import RunContext

from app.agents.response_agent import response_agent
from app.schemas.chat import *
from app.tools.retrieve_rag_context import retrieve_rag_context

router = APIRouter(prefix="/api/v1", tags=["chat"])


@router.post("/rag-retrieve")
async def rag_retrieve(request: ChatQuestion):
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
async def chat(request: ChatQuestion):

    result = await response_agent.run(
        request.question, deps=LevelContext(level=request.level)
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
