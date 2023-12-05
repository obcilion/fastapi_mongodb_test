from user_mongo_repository import UserMongoRepository # TODO: change to user interface
from user_model import User

class UserService:
    def __init__(self, user_repo: UserMongoRepository):
        self.user_repo = user_repo

    async def create_user(self, user_data: User) -> User:
        user_id = await self.user_repo.insert_user(user_data)
        user_data.id = user_id
        return user_data

   