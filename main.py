from fastapi import FastAPI
from expense_track.database import engine
import expense_track.models as models
from expense_track.routers import user

app = FastAPI()

# create all the tables while run code
models.Base.metadata.create_all(engine)

app.include_router(user.router, prefix='/user', tags=['Users'])