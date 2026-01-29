from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    nascimento = Column(String)
    cpf = Column(String)
    telefone = Column(String)
    email = Column(String, unique=True)
    senha = Column(String)
    cep = Column(String)
    rua = Column(String)
    bairro = Column(String)
    casa = Column(String)
    deficiencia = Column(String)
    genero = Column(String)

    
    


