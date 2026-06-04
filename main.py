from fastapi import FastAPI

app = FastAPI(
    title="NeoMarket B2B Service",
    description="API для панели продавца",
    version="1.0.0"
)

@app.get("/ping", tags=["Health"])
async def ping():
    return {"message": "Сервер работает"}