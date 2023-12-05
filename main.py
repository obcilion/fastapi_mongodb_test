from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request, Depends
from dotenv import load_dotenv
import os
from mongodb_connection import MongoConnector
from user_mongo_repository import UserMongoRepository
from user_model import User
from user_service import UserService


load_dotenv()
connection_string = os.getenv("MONGODB_CONNECTION_STRING")
db_name = os.getenv("MONGODB_DB_NAME")

@asynccontextmanager
async def lifespan(app: FastAPI):
    mongo_connector = MongoConnector(connection_string, db_name)
    server_info = await mongo_connector.client.server_info()
    print(f"Server info: {server_info}") # Will raise if we can't connect to the server, which is good
    user_repository = UserMongoRepository(mongo_connector)
    app.state.user_service = UserService(user_repository)
    yield
    print("Closing connection to MongoDB")
    await mongo_connector.client.close()

def get_user_service(request: Request) -> UserService:
    return request.app.state.user_service


app = FastAPI(lifespan=lifespan)

@app.post("/users/", response_model=User)
async def create_user(user_data: User, user_service: UserService = Depends(get_user_service)):
    try:
        created_user = await user_service.create_user(user_data)
    except Exception as e:
        # Handle specific exceptions as necessary
        raise HTTPException(status_code=400, detail=str(e))

    return created_user