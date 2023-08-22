import uvicorn
from decouple import config
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from apps.todo.routers import router as todo_router

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(config("DB_URL"))
    app.mongodb = app.mongodb_client[config("DB_NAME")]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(todo_router, tags=["tasks"], prefix="/task")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=config("DEBUG_MODE"),
        port=8000,
    )
