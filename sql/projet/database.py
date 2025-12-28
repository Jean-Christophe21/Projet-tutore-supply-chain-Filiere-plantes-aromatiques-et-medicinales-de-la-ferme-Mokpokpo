# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:postgres123@localhost:5433/projet_mokpokpo"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Fonction pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Vérifier la connexion
try:
    with engine.connect() as connection:
        print("✓ Connexion réussie à PostgreSQL !")
except Exception as e:
    print(f"✗ Erreur de connexion : {e}")