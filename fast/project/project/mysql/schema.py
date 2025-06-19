<<<<<<< HEAD
from pydantic import BaseModel
from typing import Optional, List

class HistoryBase(BaseModel): 
    title: str
    description: Optional[str] = None

class HistoryCreate(HistoryBase):
    pass

class History(HistoryBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel): 
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    is_active: bool
    histories: List[History] = []

    class Config:
        orm_mode = True
=======
from pydantic import BaseModel
from typing import Optional, List

class HistoryBase(BaseModel): 
    title: str
    description: Optional[str] = None

class HistoryCreate(HistoryBase):
    pass

class History(HistoryBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel): 
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    is_active: bool
    histories: List[History] = []

    class Config:
        orm_mode = True
>>>>>>> origin
