from fastapi import FastAPI
from routers import example
from models.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Template")

app.include_router(example.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
