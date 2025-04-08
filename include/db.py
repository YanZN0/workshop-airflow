from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base     # ORM para fazermos as transformações do código em Python para um código estruturado SQL.
from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_URL')
engine = create_engine(SQLALCHEMY_DATABASE_URL)     # Fazendo conexão com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)     # A varíavel SessionLocal agora é responsavel para Sessões e Conexões, com ela nos conectamos e falamos com o nosso banco.
Base = declarative_base()       # Base tem como objetivo principal fazer o ORM das tabelas criadas por código Python (classes).