import sys
import pathlib
sys.path.append(f"{pathlib.Path(__file__).parent.parent.resolve()}")
import pytest
from fastapi.testclient import TestClient
from app.routers.cocktails import search_cocktail_by_name
from app.main import app

client = TestClient(app)

def test_search_cocketail_by_name():
    response = client.get("/cocktails/search/name/Gin Sour")
    assert response.status_code == 200

    data = response.json()
    assert data['drinks'][0]['idDrink'] == '11417'
