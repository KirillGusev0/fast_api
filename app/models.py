from pydantic import BaseModel
from typing import Optional

# Схема для сущности
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

# Схема для создания 
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# Схема для обновления 
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

