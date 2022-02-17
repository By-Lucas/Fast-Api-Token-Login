from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Criar um objeto e chamar dna funcao python, forma mais simples e rapida
class Usuario(BaseModel):
    id : int
    nome : str
    senha : str

lista_user = [
    Usuario(id=1, nome='lucas', senha='senha1'),
    Usuario(id=2, nome='joao', senha='senha2'),
    Usuario(id=3, nome='marcos', senha='senha3'),
]

@app.get("/")
def main():
    return { 'inicio': 'Pagina inicial'}


@app.post("/usuario")
def user(usuario: Usuario):
    lista_user.append(usuario)
    return "usuario cadastrado"

@app.get("/usuariolistar")
def usuarios_cadastrados():
    return lista_user


@app.get("/cadastro")
def cadastro():
    return {"cadastro": "Cadastrar"}

@app.get("/login")
def login():
    return {"login": "logar"}

