from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.database import get_db

router = APIRouter(
    prefix="/example",
    tags=["example"]
)

@router.get("/")
def get_example(db: Session = Depends(get_db)):
    return {"message": "Example route"}
