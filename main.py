from fastapi import FastAPI
from expense_track.database import engine
import expense_track.models as models

app = FastAPI()

@app.post("/user/create")
def create_user():
    return "user"

# create all the tables while run code
models.Base.metadata.create_all(engine)