from fastapi import FastAPI, Request
from motor.motor_asyncio import AsyncIOMotorClient
import os

class MongoDBMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app
        self.client = None

    async def __call__(self, request: Request, call_next):
        mongo_uri = os.getenv("DATABASE_URI")
        db_name = os.getenv("DATABASE_NAME")
        self.client = AsyncIOMotorClient(mongo_uri)
        request.state.db = self.client[db_name]
        response = await call_next(request)
        request.state.db = None
        self.client.close()
        return response

    async def startup(self):
        pass
    
    async def shutdown(self):
        pass