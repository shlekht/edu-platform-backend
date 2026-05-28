from fastapi import FastAPI
from db.database import engine
from models.base import Base
from api import auth
from api import user


app = FastAPI(title="LMS API")

app.include_router(auth.router)
app.include_router(user.router)

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}



