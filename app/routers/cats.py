import requests
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db
from typing import List
from app.utils import cat_validation

router = APIRouter()
@router.post("/", response_model=schemas.CatResponse)
def create_cat(cat: schemas.CatCreate, db: Session = Depends(get_db)):
    if not cat_validation.is_valid_breed(cat.breed):
        raise HTTPException(status_code=400, detail="Invalid cat breed")
    
    existing_cat = db.query(models.Cat).filter(
        models.Cat.name == cat.name,
        models.Cat.breed == cat.breed,
        models.Cat.years_of_experience == cat.years_of_experience
    ).first()
    
    if existing_cat:
        raise HTTPException(status_code=400, detail="Cat with the same name, breed, and experience already exists.")
    
    db_cat = crud.create_cat(db, cat)
    return db_cat
    
    
@router.get("/", response_model=List[schemas.CatResponse])
def list_cats(db: Session = Depends(get_db)):
    return crud.get_cats(db)

@router.get("/{cat_id}", response_model=schemas.CatResponse)
def get_cat(cat_id: int, db: Session = Depends(get_db)):
    cat = crud.get_cat(db, cat_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Cat not found")
    return cat

@router.put("/{cat_id}", response_model=schemas.CatResponse)
def update_cat(cat_id: int, update_data: schemas.CatUpdate, db: Session = Depends(get_db)):
    cat = crud.update_cat_salary(db, cat_id, update_data.salary)
    if not cat:
        raise HTTPException(status_code=404, detail="Cat not found")
    return cat

@router.delete("/{cat_id}", response_model=schemas.CatResponse)
def delete_cat(cat_id: int, db: Session = Depends(get_db)):
    cat = crud.delete_cat(db, cat_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Cat not found")
    return cat
