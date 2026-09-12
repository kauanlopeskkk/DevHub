from fastapi import FastAPI
from fastapi.middleware import CORSMiddleware
from routes import usuarios, projetos, tarefas, bugs  # type: ignore[reportMissingImports]


app = FastAPI()

app.add_middleware(

CORSMiddleware,
allow_origins = ["*"],
allow_credentials = True,
allow_methods = ["*"],
allow_headers=["*"],

)

app.include_router(usuarios.router)

app.include_router(projetos.router)
app.include_router(tarefas.router)
app.include_router(bugs.router)