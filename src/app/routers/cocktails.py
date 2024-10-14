from fastapi import APIRouter
from app.services.cocktail_services import fetch_cocktail_by_name

router = APIRouter(
    prefix="/cocktails",
    tags = ['Cocktails'])

@router.get("/search/name/{cocktail_name}")
async def search_cocktail_by_name(cocktail_name:str):
    return await fetch_cocktail_by_name(cocktail_name)