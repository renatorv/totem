from fastapi import FastAPI

from src.core import database
from src.core.models import Base

from src.api.admin import router as admin_router
from src.api.app import router as app_router


# aqui é feita a chamada para criação das tabelas no BD
Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Totem Pro ")

app.include_router(admin_router)
app.include_router(app_router)