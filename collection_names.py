from enum import Enum

class CollectionName(str, Enum):
    users = "users"
    posts = "posts"
    comments = "comments"