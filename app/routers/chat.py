from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.chat import Question
from app.tools.rag_tool import get_rag_data

router = APIRouter(prefix="/api/v1/chat", tags=["chat"])


@router.post("/ask-question")
async def ask_question(request: Question):
    result = await get_rag_data(request.question)
    return JSONResponse(
        status_code=200,
        content={
            "code": 200,
            "message": "success",
            "result": result.model_dump(),
        },
    )
