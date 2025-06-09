import json

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic_ai import RunContext

from app.agents.answerer_agent import answerer_agent
from app.responses import response_error, response_success
from app.schemas.answerer_agent_output import AnswererAgentOutput
from app.schemas.chat import *
from app.tools.retrieve_rag_context import retrieve_rag_context

router = APIRouter(prefix="/api/v1/chat", tags=["chat"])


@router.post("/rag")
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

    return response_success(
        resources={"question": request.question, "output": result.model_dump()}
    )


@router.post("/ask")
async def ask(request: ChatQuestion) -> JSONResponse:

    result = await answerer_agent.run(
        request.question, deps=LevelContext(level=request.level)
    )
    result_dict = json.loads(result.output)
    answerer_agent_output = AnswererAgentOutput(**result_dict)

    return response_success(
        resources={
            "question": request.question,
            "result": answerer_agent_output.model_dump(),
        }
    )
