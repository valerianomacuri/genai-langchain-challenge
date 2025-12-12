from fastapi import FastAPI

from app.routers import documents, query

app = FastAPI(title="Knowledge Assistant API")

app.include_router(documents.router)
app.include_router(query.router)


@app.get("/")
async def root():
    return {"message": "Knowledge Assistant API is running"}
