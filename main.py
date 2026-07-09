from fastapi import FastAPI
from src.api.router import router
app=FastAPI(title="MAF")
app.include_router(router)