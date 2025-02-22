from fastapi import FastAPI

from src.core import database
from src.core.models import Base
from src.routes.stores import router as stores_router
from src.routes.products import router as products_router

# aqui é feita a chamada para criação das tabelas no BD
Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Totem Pro ")

app.include_router(stores_router)
app.include_router(products_router)
