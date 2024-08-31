from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.routers import user
from app.db import MongoDBMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

mongo_middleware = MongoDBMiddleware(app)
app.add_event_handler("startup", mongo_middleware.startup)
app.add_event_handler("shutdown", mongo_middleware.shutdown)
app.middleware('http')(mongo_middleware)

app.include_router(user.router, tags=['Users'], prefix='/api/users')

@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}