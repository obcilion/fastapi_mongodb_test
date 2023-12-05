from pydantic import BaseModel, Field
from typing import Optional
from mongo_pydantic_utils import PyObjectId

class User(BaseModel):
    # Optional because we don't have an id until we create the user in mongo
    id: Optional[PyObjectId] = Field(None, alias='_id')
    name: str
    email: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: str}
