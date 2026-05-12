from fastapi import FastAPI
from db.database import engine
from models.base import Base
from api import auth


app = FastAPI(title="LMS API")

app.include_router(auth.router)

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}



