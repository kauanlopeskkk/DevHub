from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas

router = APIRouter(
    prefix="/projetos",
    tags=["projetos"],
)


@router.post("/", response_model=schemas.ProjetoResponse)
def criar_projeto(projeto: schemas.ProjetoCriar, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == projeto.usuario_id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")

    novo_projeto = models.Projeto(
        nome=projeto.nome,
        descricao=projeto.descricao,
        status=projeto.status,
        usuario_id=projeto.usuario_id,
    )

    db.add(novo_projeto)
    db.commit()
    db.refresh(novo_projeto)
    return novo_projeto


@router.get("/", response_model=list[schemas.ProjetoResponse])
def listar_projetos(db: Session = Depends(get_db)):
    projetos = db.query(models.Projeto).all()
    return projetos


@router.get("/{projeto_id}", response_model=schemas.ProjetoResponse)
def buscar_projeto(projeto_id: int, db: Session = Depends(get_db)):
    projeto = db.query(models.Projeto).filter(models.Projeto.id == projeto_id).first()

    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    return projeto


@router.put("/{projeto_id}", response_model=schemas.ProjetoResponse)
def atualizar_projeto(
    projeto_id: int,
    dados: schemas.ProjetoCriar,
    db: Session = Depends(get_db),
):
    projeto = db.query(models.Projeto).filter(models.Projeto.id == projeto_id).first()

    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    # (Opcional) Se você quiser validar usuario_id ao atualizar, faça a checagem aqui.
    projeto.nome = dados.nome
    projeto.descricao = dados.descricao
    projeto.status = dados.status
    projeto.usuario_id = dados.usuario_id

    db.commit()
    db.refresh(projeto)
    return projeto


@router.delete("/{projeto_id}")
def excluir_projeto(projeto_id: int, db: Session = Depends(get_db)):
    projeto = db.query(models.Projeto).filter(models.Projeto.id == projeto_id).first()

    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    db.delete(projeto)
    db.commit()
    return {"detail": "Projeto excluído com sucesso"}
