from fastapi import FastAPI
from server_app.api.endpoints import items
from server_app.db.base import init_db

app = FastAPI()

# Include routers
app.include_router(items.router, prefix="/api/v1")
# Initialize database
@app.on_event("startup")
def on_startup():
    init_db()
