import uvicorn
from fastapi import FastAPI
from routes.rotas import r
from services.main import create_spark_session
import time

app = FastAPI()
app.include_router(r)
uvicorn.run(app, host='localhost', port='7777')