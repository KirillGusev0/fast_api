from typing import Dict
from .models import Item

# Хранилище в памяти (ключ = id)
items_db: Dict[int, Item] = {}

