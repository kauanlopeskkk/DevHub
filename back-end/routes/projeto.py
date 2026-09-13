from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from database import get_db
router = APIRouter(
    prefix="/projetos",
    tags=["projetos"]
)

@router.post("/", response_model=schemas.ProjetoResponse)
def criar_projeto(projeto: schemas.ProjetoCriar, db: Session = Depends (get_db)
):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first() 

if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    novo_projeto = models.Projeto(
        nome=projeto.nome,