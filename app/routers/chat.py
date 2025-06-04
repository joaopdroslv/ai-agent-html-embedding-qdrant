from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic_ai import RunContext

from app.schemas.chat import *
from app.tools.retrieve_rag_context import retrieve_rag_context
from app.agents.response_agent import response_agent

router = APIRouter(prefix="/api/v1", tags=["chat"])


@router.post("/rag-retrieve")
async def rag_retrieve(request: ChatQuestion):
    # This is a simpler operation, not yet integrated with an AI agent.

    context = RunContext(  # Dummy context
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

    result = await response_agent.run(request.question, deps=LevelContext(level=request.level))

    return JSONResponse(
        status_code=200,
        content={
            "code": 200,
            "message": "success",
            "question": request.question,
            "result": result.model_dump(),
        },
    )