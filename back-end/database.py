from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker

DATABASE_URL = "sqlite:///./devhub.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def init_db() -> None:
    # Cria as tabelas conforme os modelos definidos em `models.py`.
    # Importante para testes locais (principalmente no SQLite).
    from models import Usuario, Projeto, Tarefa, Bug  # noqa: F401

    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()