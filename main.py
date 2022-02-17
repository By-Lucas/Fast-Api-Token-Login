from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from models import CONN,  Pessoa, Tokens 
from secrets import token_hex


app = FastAPI()

# Conectar com banco de dados
def conectaBanco():
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

@app.post('/cadastro')
def cadastro(nome: str, user: str, senha: str, sobrenome: str, cpf_cnpj: int, email: str, endereco:str,cidade:str,numero_casa:int, estado:str):
    session = conectaBanco()
    # Buscar todo os usuario e senha da tabela
    usuario = session.query(Pessoa).filter_by(usuario=user, senha=senha, cpf_cnpj=cpf_cnpj, email=email).all()
    if len(usuario) == 0:
        x = Pessoa(nome=nome, 
                    usuario=user, 
                    senha=senha, 
                    sobrenome=sobrenome, 
                    cpf_cnpj=cpf_cnpj, 
                    email=email,
                    endereco=endereco,
                    cidade=cidade,
                    numero_casa=numero_casa,
                    estado=estado)
        session.add(x)
        session.commit()
        return {'status': 'Usuário cadastrado'}
    elif len(usuario) > 0:
        return {'status': 'Usuário já cadastrado'}

@app.post('/login')
def login_token(usuario: str, senha:str):
    session = conectaBanco()
    user = session.query(Pessoa).filter_by(usuario=usuario, senha=senha).all()
    if len(usuario) == 0:
        return {'status': 'Usuário inexistente'}
    
    while True:
        token = token_hex(50) #Gerar um token com 50 caracteres
        tokenExiste = session.query(Tokens).filter_by(token=token).all()
        if len(tokenExiste) == 0:
            pessoaExite = session.query(Tokens).filter_by(id_pessoa=user[0].id).all() #inserir token
            if len(pessoaExite) == 0:
                novoToken = Tokens(id_pessoa=user[0].id, token=token) #Se o token nao existir ele cadasta um novo
                session.add(novoToken)
            elif len(pessoaExite) > 0:
                pessoaExite[0].token = token
            
            session.commit()
            break
    return token

@app.get('/usuarios')
def Todos_usuarios():
    conecta = conectaBanco()
    usuarios_todos = conecta.query(Pessoa).all()

    return usuarios_todos
