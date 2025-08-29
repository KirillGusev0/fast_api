from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from .models import Item, ItemCreate, ItemUpdate
from .storage import items_db
from fastapi.responses import HTMLResponse

app = FastAPI(title="Test API", description="Тестовое API на FastAPI", version="1.0.0")


@app.get("/", response_class=HTMLResponse, summary="Домашняя страница")
def root():
    return """
    <html>
        <head>
            <title>Добро пожаловать в Test API</title>
        </head>
        <body>
            <h1>Добро пожаловать в Test API 🚀</h1>
            <p>Выберите один из разделов документации:</p>
            <ul>
                <li><a href="/docs">Swagger UI</a></li>
                <li><a href="/redoc">ReDoc</a></li>
            </ul>
            <p>Доступные ресурсы API:</p>
            <ul>
                <li><a href="/items">/items</a> — список сущностей</li>
            </ul>
        </body>
    </html>
    """

@app.get("/items", response_model=List[Item], summary="Получить список всех Items")
def list_items(min_price: Optional[float] = Query(None, description="Фильтр: минимальная цена"),
               max_price: Optional[float] = Query(None, description="Фильтр: максимальная цена")):
    
    result = list(items_db.values())
    if min_price is not None:
        result = [i for i in result if i.price >= min_price]
    if max_price is not None:
        result = [i for i in result if i.price <= max_price]
    return result


@app.get("/items/{item_id}", response_model=Item, summary="Получить один Item")
def get_item(item_id: int):
    
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


@app.post("/items", response_model=Item, status_code=201, summary="Создать новый Item")
def create_item(item: ItemCreate):
    
    new_id = max(items_db.keys(), default=0) + 1
    new_item = Item(id=new_id, **item.dict())
    items_db[new_id] = new_item
    return new_item


@app.put("/items/{item_id}", response_model=Item, summary="Обновить Item")
def update_item(item_id: int, item: ItemUpdate):
    
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    stored_item = items_db[item_id]
    updated_data = item.dict(exclude_unset=True)
    updated_item = stored_item.copy(update=updated_data)
    items_db[item_id] = updated_item
    return updated_item


@app.delete("/items/{item_id}", status_code=204, summary="Удалить Item")
def delete_item(item_id: int):
    
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return
