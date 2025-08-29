from pydantic import BaseModel
from typing import Optional

# Схема для сущности (например, "Item")
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

# Схема для создания (id не передаётся — назначаем сами)
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# Схема для обновления (все поля опциональны)
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
