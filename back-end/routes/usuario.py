from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
router = APIRouter(
    tags=["usuarios"]
)

@router.post("/", response_model=schemas.UsuarioResponse)
def criar_usuario(usuario: schemas.UsuarioCriar, db: Session = Depends(get_db)):
    usuario_existente = db.query(models.Usuario).filter(
        models.Usuario.email == usuario.email
    ).first()

    if usuario_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    novo_usuario = models.Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=usuario.senha
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario

@router.post("/login", response_model= schemas.UsuarioResponse
)
def login_usuario(usuario: schemas.UsuarioLogin, db: Session = Depends(get_db)):

    usuario_existente = db.query(models.Usuario).filter(
        models.Usuario.email == usuario.email
    ).first()

    if not usuario_existente or usuario_existente.senha != usuario.senha:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos")

    return usuario_existente

@router.get("/",response_model=list[schemas.UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(models.Usuario).all()
    return usuarios

def buscar_usuario_por_id(usuario_id: int, db: Session):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

