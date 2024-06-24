from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi import FastAPI
from server_app.api.endpoints import items
from server_app.db.base import init_db

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This will run on startup
    init_db()
    yield
    # This will run on shutdown (if any cleanup needed, add here)

app = FastAPI(lifespan=lifespan)


# Include routers
app.include_router(items.router, prefix="/api/v1")
