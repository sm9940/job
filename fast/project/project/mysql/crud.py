from sqlalchemy.orm import Session
from . import models, schema

############################ USER ############################
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip:int=0, limit:int=50):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user:schema.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def update_user(db: Session, user: models.User, updated_user: schema.UserCreate):
    for key, value in updated_user.model_dump().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user: models.User):
    db.delete(user)
    db.commit()
############################ History ############################
def get_History(db: Session, History_id: int):
    return db.query(models.History).filter(models.History.id == History_id).first()

def get_Histories(db: Session, skip:int=0, limit: int=50):
    return db.query(models.History).offset(skip).limit(limit).all()

def create_user_History(db:Session, History:schema.HistoryCreate, user_id : int):
    db_History = models.History(**History.model_dump(), owner_id=user_id )
    db.add(db_History)
    db.commit()
    db.refresh(db_History)
    return db_History

def update_History(db: Session, History: models.History, updated_History: schema.HistoryCreate):
    for key, value in updated_History.model_dump().items():
        setattr(History, key, value)
    db.commit()
    db.refresh(History)
    return History

def delete_History(db: Session, History: models.History):
    db.delete(History)
    db.commit()

