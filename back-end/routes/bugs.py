from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
router = APIRouter(
    prefix="/bugs",
    tags=["bugs"]

)

@router.post("/", response_model=list[schemas.BugResponse],status_code=201)
def criar_bug(bug: schemas.BugCriar, db: Session = Depends(get_db)):

    projeto = db.query(models.Projeto).filter(models.Projeto.id == bug.projeto_id).first()
    if not projeto:
        raise HTTPException(
            status_code=404, 
            detail= "Projeto não encontrado para registrar o bug"

        )
    novo_bug = models.Bug(
        titulo = bug.titulo,
        descricao = bug.descricao,
        prioridade = bug.prioridade,
        status = bug.status,
        projeto_id = bug.projeto_id
    )
    db.add(novo_bug)
    db.commit()
    db.refresh(novo_bug)
    return novo_bug

@router.get("/", response_model=list[schemas.BugResponse])
def listar_bugs(

    projeto_id: int | None = None,
    status_bug: str | None = None,
    db: Session = Depends(get_db)

):
    query = db.query(models.Bug)

    if projeto_id is not None:
        query = query.filter(models.Bug.projeto_id == projeto_id)

    if status_bug is not None:
        query = query.filter(models.Bug.status == status_bug)

    return query.all()


@router.get("/{bug_id}", response_model=schemas.BugResponse)
def buscar_bug(bug_id: int, db: Session = Depends(get_db)):
    bug = db.query(models.Bug).filter(models.Bug.id == bug_id).first()

    if not bug:
        raise HTTPException(
            status_code=404, detail="Bug não encontrado"
        )
    return bug

@router.put("/{bug_id}", response_model=schemas.BugResponse)
def atualizar_Bug(
    bug_id: int, dados: schemas.BugCriar, db: Session = Depends(get_db)
):
    bug = db.query(models.Bug).filter(models.Bug.id == bug_id).first()
    if not bug:
        raise HTTPException(status_code=404, detail="Bug não encontrado")

    bug.titulo = dados.titulo
    bug.descricao = dados.descricao
    bug.prioridade = dados.prioridade
    bug.status = dados.status
    bug.projeto_id = dados.projeto_id
    db.commit()
    db.refresh(bug)
    return bug


@router.delete("/{bug_id}", status_code=status.HTTP_200_OK)
def excluir_bug(bug_id: int, db: Session = Depends(get_db)):
    bug = db.query(models.Bug).filter(models.Bug.id == bug_id).first()
    if not bug:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Bug não encontrado"
        )
    db.delete(bug)
    db.commit()
    return {"detail": "Bug excluído com sucesso"}