import sys
import pathlib
sys.path.append(f"{pathlib.Path(__file__).parent.parent.resolve()}")
import pytest
from httpx import AsyncClient
import asyncio
from app.services.cocktail_services import fetch_cocktail_by_name

@pytest.mark.asyncio
async def test_fetch_cocktail_by_name():
    data = await fetch_cocktail_by_name("margarita")
    assert data['drinks'][0]['idDrink']=='11007'
    assert data['drinks'][1]['strDrink'] == "Blue Margarita"

async def print_api_response():
    response = await fetch_cocktail_by_name("Gin Sour")
    print(response)

asyncio.run(print_api_response())