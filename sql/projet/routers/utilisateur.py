from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import sys
sys.path.insert(0, '/home/sly/Documents/s5/projet tutoré/projet')

from models.model import Utilisateur
from schema.utilisateur import UtilisateurCreate, UtilisateurOut
from database import get_db

router = APIRouter(prefix="/utilisateurs", tags=["Utilisateurs"])

@router.post("/", response_model=UtilisateurOut)
def create_utilisateur(user: UtilisateurCreate, db: Session = Depends(get_db)):
    db_user = Utilisateur(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=list[UtilisateurOut])
def get_utilisateurs(db: Session = Depends(get_db)):
    return db.query(Utilisateur).all()