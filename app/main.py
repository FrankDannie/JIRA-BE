from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api import router as api_router
from app.db.base import Base, engine

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# CORS configuration
origins = [
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
