from sqlalchemy.orm import Session
from . import models, schemas

def get_cat(db: Session, cat_id: int):
    return db.query(models.Cat).filter(models.Cat.id == cat_id).first()

def get_cats(db: Session):
    return db.query(models.Cat).all()

def create_cat(db: Session, cat: schemas.CatCreate):
    db_cat = models.Cat(**cat.dict())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def update_cat_salary(db: Session, cat_id: int, salary: float):
    db_cat = get_cat(db, cat_id)
    if db_cat:
        db_cat.salary = salary
        db.commit()
        db.refresh(db_cat)
    return db_cat

def delete_cat(db: Session, cat_id: int):
    db_cat = get_cat(db, cat_id)
    if db_cat:
        db.delete(db_cat)
        db.commit()
    return db_cat

def create_mission(db: Session, mission_data: schemas.MissionCreate):
    mission = models.Mission()
    db.add(mission)
    db.commit()
    db.refresh(mission)

    for target_data in mission_data.targets:
        target = models.Target(**target_data.dict(), mission_id=mission.id)
        db.add(target)
    db.commit()
    return mission

def get_mission(db: Session, mission_id: int):
    return db.query(models.Mission).filter(models.Mission.id == mission_id).first()

def get_missions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Mission).offset(skip).limit(limit).all()

def assign_cat_to_mission(db: Session, mission_id: int, cat_id: int):
    mission = get_mission(db, mission_id)
    cat = get_cat(db, cat_id)
    
    if mission and cat and not mission.cat_id:  
        mission.cat_id = cat_id 
        db.commit() 
        db.refresh(mission)  
        return mission
    else:
        return None  
