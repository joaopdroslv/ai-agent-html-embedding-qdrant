from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.modules.embeddings import (
    get_all_embeddings_articles,
    get_all_embeddings_as_dicts,
    get_all_embeddings_categories,
    get_all_embeddings_levels,
)
from app.responses import response_error, response_success

router = APIRouter(prefix="/api/v1/embeddings", tags=["embeddings"])


@router.get("/")
async def embeddings() -> JSONResponse:

    embeddings = get_all_embeddings_as_dicts()

    return response_success(resources={"embeddings": embeddings})


@router.get("/articles")
async def articles() -> JSONResponse:

    articles = get_all_embeddings_articles()
    articles_dicts = [article.model_dump() for article in articles]

    return response_success(resources={"articles": articles_dicts})


@router.get("/filters")
async def filters() -> JSONResponse:

    categories = get_all_embeddings_categories()
    categories_dicts = [category.model_dump() for category in categories]

    levels = get_all_embeddings_levels()
    levels_dicts = [level.model_dump() for level in levels]

    return response_success(
        resources={"categories": categories_dicts, "levels": levels_dicts},
    )
