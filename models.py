# models.py - Completo pro seu cadastro candidato
from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Usuario(Base):
    __tablename__ = "Usuarios"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    nascimento = Column(String(10), nullable=False)  # dd/mm/aaaa
    cpf = Column(String(14), unique=True, nullable=False)  # 000.000.000-00
    telefone = Column(String(15), nullable=False)  # (99) 99999-9999
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)  # Hash bcrypt
    cep = Column(String(9), nullable=False)  # 00000-000
    rua = Column(String(100), nullable=False)
    bairro = Column(String(100), nullable=False)
    numero_casa = Column(String(10), nullable=False)
    deficiencia = Column(String(50), nullable=False)
    genero = Column(String(30), nullable=False)
    
    # Relacionamentos futuros (cursos, vagas salvas)
    # cursos = relationship("CursoInscrito", back_populates="candidato")
    # vagas_salvas = relationship("VagaSalva", back_populates="candidato")

# Se tiver outras tabelas (ex: empresas, cursos)
# class Empresa(Base):
#     __tablename__ = "empresas"
#     id = Column(Integer, primary_key=True, index=True)
#     nome = Column(String(100), nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     senha = Column(String(255), nullable=False)
#     cnpj = Column(String(18), unique=True, nullable=False)

# Rode uma vez pra criar tabelas:
# python -c "from database import engine; from models import Base; Base.metadata.create_all(bind=engine)"


