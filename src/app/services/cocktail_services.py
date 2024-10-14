import httpx
import os

BASE_URL = "https://thecocktaildb.com/api/json/v1/1"

async def fetch_cocktail_by_name(cocktail_name:str):
    url = f"{BASE_URL}/search.php?s={cocktail_name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()
