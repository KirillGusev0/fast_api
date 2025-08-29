from typing import Dict
from .models import Item

# Простое хранилище в памяти (ключ = id)
items_db: Dict[int, Item] = {}
