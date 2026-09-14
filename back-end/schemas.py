from pydantic import BaseModel,ConfigDict,Field

class UsuarioCriar(BaseModel):
    nome: str
    email: str
    senha: str

class UsuarioLogin(BaseModel):
    email: str
    senha: str

class ProjetoCriar(BaseModel):
    nome: str
    descricao: str
    status: str
    usuario_id: int

class UsuarioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    nome: str
    email: str

class ProjetoCriar(BaseModel):
    nome: str
    descricao: str
    status: str = "Em andamento"

class ProjetoResponse(BaseModel):
    id: int
    nome: str
    descricao: str
    status: str
    usuario_id: int

    model_config = ConfigDict(from_attributes=True)

class TarefaCriar(BaseModel):
    titulo: str
    descricao: str
    prioridade: str
    status: str = "Pendente"
    projeto_id: int

class TarefaResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    prioridade: str
    status: str
    projeto_id: int

    model_config = ConfigDict(from_attributes=True)


class BugCriar(BaseModel):
    titulo: str
    descricao: str
    prioridade: str
    status: str = "Aberto"
    projeto_id: int

class BugResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    prioridade: str
    status: str
    projeto_id: int

    model_config = ConfigDict(from_attributes=True)


    