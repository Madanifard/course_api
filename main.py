from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import MongoDBManager
from routers import instructor
from routers import course


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

app.include_router(instructor.router, prefix="/instructor", tags=["instructors"])
app.include_router(course.router, prefix="/course", tags=["courses"])