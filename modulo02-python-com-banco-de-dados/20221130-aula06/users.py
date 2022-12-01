
from database import engine, Base, session
from models import User

if __name__ == "__main__":

    # Cria as tabelas definidas no módulo models.py
    Base.metadata.create_all(engine)
