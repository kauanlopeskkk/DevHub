from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter(
    prefix="/tarefas",
    tags=["tarefas"]
)


@router.post("/", response_model=schemas.TarefaResponse, status_code=201)
def criar_tarefa(tarefa: schemas.TarefaCriar, db: Session = Depends(get_db)):
    # Valida se o projeto vinculado à tarefa realmente existe
    projeto = db.query(models.Projeto).filter(models.Projeto.id == tarefa.projeto_id).first()
    if not projeto:
        raise HTTPException(
            status_code=404, 
            detail="Projeto não encontrado para associar a tarefa"
        )

    nova_tarefa = models.Tarefa(
        nome=tarefa.nome,
        descricao=tarefa.descricao,
        status=tarefa.status,
        projeto_id=tarefa.projeto_id
    )
    
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa



@router.get("/", response_model=list[schemas.TarefaResponse])
def listar_tarefas(projeto_id: int | None = None, db: Session = Depends(get_db)):
    query = db.query(models.Tarefa)
    
    # Se passar ?projeto_id=1 na URL, lista apenas as tarefas desse projeto
    if projeto_id is not None:
        query = query.filter(models.Tarefa.projeto_id == projeto_id)
        
    return query.all()


# 3. BUSCAR TAREFA POR ID
@router.get("/{tarefa_id}", response_model=schemas.TarefaResponse)
def buscar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(
            status_code=404, 
            detail="Tarefa não encontrada"
        )
    return tarefa



@router.put("/{tarefa_id}", response_model=schemas.TarefaResponse)
def atualizar_tarefa(tarefa_id: int, dados: schemas.TarefaCriar, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(
            status_code=404, 
            detail="Tarefa não encontrada"
        )

    # Atualiza os dados
    tarefa.nome = dados.nome
    tarefa.descricao = dados.descricao
    tarefa.status = dados.status
    tarefa.projeto_id = dados.projeto_id

    db.commit()
    db.refresh(tarefa)
    return tarefa



@router.delete("/{tarefa_id}", status_code=200)
def excluir_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(
            status_code=404, 
            detail="Tarefa não encontrada"
        )

    db.delete(tarefa)
    db.commit()
    return {"detail": "Tarefa excluída com sucesso"}