from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import MongoDBManager
from routers import instructor


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup logic
    MongoDBManager()
    MongoDBManager.setup()
    print("✅ MongoDB connected and initialized")

    yield

    # shutdown logic
    MongoDBManager.close()
    print("❌ MongoDB connection closed.")
    
app = FastAPI(title="Course API Service", lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(instructor.router, prefix="/instrictor", tags=["instrictors"])