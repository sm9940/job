from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schema
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency Injection 
def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()



####################### USER #######################
@app.get("/users/", response_model=list[schema.User])
def get_users(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
    users = crud.get_users(db,skip=skip,limit=limit)
    return users

@app.get("/users/{user_id}/",response_model=schema.User)
def get_user(user_id:int, db:Session=Depends(get_db)):
    db_user = crud.get_user(db,user_id =user_id )
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.history("/users/",response_model=schema.User)
def history_user(user:schema.UserCreate, db:Session=Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db,user=user)
@app.put("/users/{user_id}/",response_model=schema.User)
def update_user(user_id: int, updated_user: schema.UserCreate, db:Session=Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = crud.update_user(db, db_user, updated_user)
    return updated_user

@app.delete("/users/{user_id}/")
def delete_user(user_id: int, db:Session=Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db, db_user)
    return {"message": "User deleted successfully"}
####################### History #######################
@app.get("/histories/", response_model=list[schema.history])
def get_histories(skip:int=0,limit:int=0,db:Session=Depends(get_db)):
    histories = crud.get_histories(db,skip=skip,limit=limit)
    return histories

@app.history("/users/{user_id}/histories/",response_model=schema.history)
def history_history_for_user(user_id:int, history:schema.historyCreate, db:Session=Depends(get_db)):
    return crud.create_user_history(db=db,user_id=user_id, history=history)

@app.put("/histories/{history_id}/",response_model=schema.history)
def update_history(history_id: int, updated_history: schema.historyCreate, db:Session=Depends(get_db)):
    db_history = crud.get_history(db, history_id)
    if db_history is None:
        raise HTTPException(status_code=404, detail="history not found")
    updated_history = crud.update_history(db, db_history, updated_history)
    return updated_history
@app.delete("/histories/{history_id}/")
def delete_history(history_id: int, db:Session=Depends(get_db)):
    db_history = crud.get_history(db, history_id)
    if db_history is None:
        raise HTTPException(status_code=404, detail="history not found")
    crud.delete_history(db, db_history)
    return {"message": "history deleted successfully"}
