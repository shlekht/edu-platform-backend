from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine
from models.base import Base
from api import auth, users, courses, notes, chat, history


app = FastAPI(title="LMS API")


origins = [
    "http://localhost:5173",    
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            
    allow_credentials=True,           
    allow_methods=["*"],              
    allow_headers=["*"],              
)


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(courses.router)
app.include_router(notes.router)
app.include_router(chat.router)
app.include_router(history.router)

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}



