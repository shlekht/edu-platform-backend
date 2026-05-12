from fastapi import FastAPI
from db.database import engine
from models.base import Base
import models

app = FastAPI(title="LMS API")


Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}



