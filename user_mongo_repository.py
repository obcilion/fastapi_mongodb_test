from mongodb_connection import MongoConnector
from collection_names import CollectionName
from user_model import User

class UserMongoRepository:
    def __init__(self, mongo_connector: MongoConnector) -> None:
        self.collection = mongo_connector.get_collection(CollectionName.users)
    
    async def insert_user(self, user_data: User) -> str:
        result = await self.collection.insert_one(user_data.model_dump(by_alias=True))
        return result.inserted_id