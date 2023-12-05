import motor.motor_asyncio
from collection_names import CollectionName

class MongoConnector:
    def __init__(self, connection_string, db_name) -> None:
        self.client = motor.motor_asyncio.AsyncIOMotorClient(connection_string)
        self.db = self.client[db_name]

    def get_collection(self, collection_name: CollectionName):
        return self.db[collection_name]