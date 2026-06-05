from fastapi import FastAPI
from app.api.auth import router as auth_router

app = FastAPI(
    title="NeoMarket B2B Service",
    description="API для панели продавца",
    version="1.0.0"
)

app.include_router(auth_router)

@app.get("/ping", tags=["Health"])
async def ping():
    return {"message": "Сервер работает"}