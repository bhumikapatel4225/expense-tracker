from expense_track.schemas import ShowUser, User    
from fastapi import status, Depends, APIRouter, HTTPException, Response
from sqlalchemy.orm import Session
from expense_track.database import get_db
from expense_track.models import User as UserModel
from typing import List

router = APIRouter()

@router.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: User, db: Session = Depends(get_db)):
    new_user = UserModel(name=request.name, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", response_model=List[ShowUser], status_code=status.HTTP_200_OK)
def show_all_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_user_by_id(id, response: Response, db: Session = Depends(get_db)):
    users = db.query(UserModel).filter(UserModel.id == id).first()
    if users:
        return users
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} is not available!")