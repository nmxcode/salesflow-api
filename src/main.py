from fastapi import FastAPI
from src.routers import customer

app = FastAPI(
    title="SalesFlow API",
    description="A professional API for managing customers",
    version="1.0.0",
)

app.include_router(customer.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def home():
    return {
        "message": "Welcome to SalesFlow API",
        "project": "SalesFlow",
        "version": "1.0.0",
    }