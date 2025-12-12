from fastapi import APIRouter
from pydantic import BaseModel

from app.services.query_service import answer_query
from app.shared.logging import logger

router = APIRouter()


class QueryRequest(BaseModel):
    query: str


@router.post("/query")
async def query_endpoint(request: QueryRequest):
    response = answer_query(request.query)
    logger.info(f"Query: {request.query}")
    return {"query": request.query, "answer": response}
