from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.chat import Question
from app.tools.retrieve_rag_context import retrieve_rag_context

router = APIRouter(prefix="/api/v1/chat", tags=["chat"])


@router.post("/ask-question")
async def ask_question(request: Question):
    # This is a simpler operation, not yet integraed with an AI agent.
    result = await retrieve_rag_context(request.question)
    return JSONResponse(
        status_code=200,
        content={
            "code": 200,
            "message": "success",
            "question": request.question,
            "result": result.model_dump(),
        },
    )
