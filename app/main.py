from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api import router as api_router
from app.db.base import Base, engine
from app.models.user import User  
from app.models.attachment import Attachment
from app.models.comment import Comment
from app.models.task import Task
from app.models.notification import Notification
from app.models.project import Project

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# CORS configuration
origins = [
    "https://master.d1lswex6c2jyh0.amplifyapp.com",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    """
    Root endpoint for the FastAPI application.

    Returns:
        dict: A simple message indicating that the API is up and running.
    """
    return {"message": "API is up and running"}
