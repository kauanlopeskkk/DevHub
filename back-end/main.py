from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import usuario, projeto, tarefas, bugs

from database import init_db


app = FastAPI()


# Inicializa o banco (SQLite) criando as tabelas se ainda não existirem.
init_db()

app.add_middleware(

CORSMiddleware,
allow_origins = ["*"],
allow_credentials = True,
allow_methods = ["*"],
allow_headers=["*"],

)

app.include_router(usuario.router, prefix="/usuarios")

app.include_router(projeto.router)
app.include_router(tarefas.router)
app.include_router(bugs.router)
