# Fast api
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

# Database
from sqlalchemy.orm import Session

# Models and DTOs

# Services

# Other
import asyncio
import time
from uuid import uuid4

query_router = APIRouter(
  prefix="/query",
  tags=["chatbot"]
)

@query_router.post("/")
async def pull_information():
    # Process the query - tokenizer - as it's done with the indexing
    # Call retrieval function f(q,d) - search_engine/retriever
    # Return the relevant documents
    ...

