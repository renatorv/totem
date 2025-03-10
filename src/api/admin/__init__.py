from fastapi import APIRouter

from src.api.admin.routes.stores import router as stores_router
from src.api.admin.routes.products import router as products_router
from src.api.admin.routes.users import router as users_router
from src.api.admin.routes.auth import router as auth_router

router = APIRouter(prefix="/admin")

router.include_router(stores_router)
router.include_router(products_router)
router.include_router(users_router)
router.include_router(auth_router)