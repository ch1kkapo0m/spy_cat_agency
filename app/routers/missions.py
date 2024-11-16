from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.MissionResponse)
def create_mission(mission: schemas.MissionCreate, db: Session = Depends(get_db)):
    return crud.create_mission(db, mission)

@router.get("/", response_model=List[schemas.MissionResponse])
def list_missions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_missions(db, skip=skip, limit=limit)

@router.get("/{mission_id}", response_model=schemas.MissionResponse)
def get_mission(mission_id: int, db: Session = Depends(get_db)):
    mission = crud.get_mission(db, mission_id)
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission

@router.delete("/{mission_id}", response_model=schemas.MissionResponse)
def delete_mission(mission_id: int, db: Session = Depends(get_db)):
    mission = crud.delete_mission(db, mission_id)
    if not mission:
        raise HTTPException(status_code=400, detail="Mission cannot be deleted if assigned to a cat")
    return mission

@router.put("/{mission_id}/targets/{target_id}", response_model=schemas.TargetResponse)
def update_target(mission_id: int, target_id: int, target: schemas.TargetCreate, db: Session = Depends(get_db)):
    updated_target = crud.update_target(db, mission_id, target_id, target)
    if not updated_target:
        raise HTTPException(status_code=400, detail="Cannot update notes if the target or mission is completed")
    return updated_target

@router.put("/{mission_id}/targets/{target_id}/complete", response_model=schemas.TargetResponse)
def mark_target_complete(mission_id: int, target_id: int, db: Session = Depends(get_db)):
    target = crud.mark_target_complete(db, mission_id, target_id)
    if not target:
        raise HTTPException(status_code=404, detail="Target not found")
    return target

@router.put("/{mission_id}/assign-cat/{cat_id}", response_model=schemas.MissionResponse)
def assign_cat_to_mission(mission_id: int, cat_id: int, db: Session = Depends(get_db)):
    mission = crud.assign_cat_to_mission(db, mission_id, cat_id)
    if not mission:
        raise HTTPException(status_code=400, detail="Mission already has a cat assigned or invalid mission/cat")
    return mission

