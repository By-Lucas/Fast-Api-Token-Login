from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

#Conexão com banco de dados Mysql
USUARIO = 'mestredb'
SENHA = 'Mestre.2022'
HOST = 'servidormestre.mysql.uhserver.com'
BANCO = 'servidormestre'
PORT = '3306'
CHARSET = 'utf8mb4'


# Conexão com banco de dados Mysql
CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

# Conexão com sqlite (criado na pasta base)
#CONN = "sqlite:///sqlite.db"


engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# FIM DE CONEXÃO COM BANCO DE DADOS ============

# Criar tabela
class Pessoa(Base):
    __tablename__ = 'Pessoa' # Nome da tabla
    id  = Column(Integer, primary_key=True)
    nome = Column(String(50))
    sobrenome = Column(String(50))
    email = Column(String(50))
    cpf_cnpj = Column(Integer())
    endereco = Column(String(11))
    cidade = Column(String(11))
    numero_casa = Column(Integer())
    estado = Column(String(11))
    usuario = Column(String(20))
    senha = Column(String(30))

class Tokens(Base):
    __tablename__ = 'Tokens'
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('Pessoa.id')) #Vai armazenar o id da pessoa criada na tabela Pessoa
    token = Column(String(100))
    data = Column(DateTime, default=datetime.datetime.utcnow())

Base.metadata.create_all(engine)

