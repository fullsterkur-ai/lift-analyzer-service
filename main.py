from fastapi import FastAPI

from src.routes import general

app = FastAPI()

app.include_router(general.router)
