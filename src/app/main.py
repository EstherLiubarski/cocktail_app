from fastapi import FastAPI
from app.routers import cocktails

app=FastAPI()

app.include_router(cocktails.router)

# @app.get("/text_cocktail/{cocktail_name}")
# async def test_cocktail_search(cocktail_name:str):
#     try:
#         data = await fetch_cocktails