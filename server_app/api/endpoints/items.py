from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from server_app import crud
from server_app.schemas import item as item_schemas
from server_app.db.session import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/items/", response_model=item_schemas.Item)
def create_item(item: item_schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@router.get("/items/{item_id}", response_model=item_schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.get("/items/", response_model=list[item_schemas.Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
