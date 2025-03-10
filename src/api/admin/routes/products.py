from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("")
def list_products():
    return []