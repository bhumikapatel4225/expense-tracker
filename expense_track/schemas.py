from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    class config():
        arbitrary_types_allowed = True