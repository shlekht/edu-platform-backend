from fastapi import FastAPI
from db.database import engine
from models.base import Base
from api import auth
from api import users
from api import courses


app = FastAPI(title="LMS API")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(courses.router)

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}



