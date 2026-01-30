from fastapi import FastAPI, Form, Request, Cookie
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Depends, HTTPException

from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Optional

# Seus arquivos existentes
from database import SessionLocal, engine
from models import Base, Usuario

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request: Request, usuario: str | None = Cookie(None)):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            #se existir um cookie(cookie =usuario), logado = true
            "logado": usuario is not None,
            "usuario": usuario
        }
    )



# Pydantic pro JSON do frontend
class CadastroUsuario(BaseModel):
    nome: str = ""
    nascimento: str = ""
    cpf: str = ""
    tel: str = ""
    email: str = ""
    senha: str = ""  # HASH aqui depois!
    cep: str = ""
    rua: str = ""
    bairro: str = ""
    numero: str = ""
    deficiencia: str = ""
    genero: str = ""

# Dependency pro DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/cadastro")
async def cadastro_usuario(
    dados: CadastroUsuario,  # Recebe JSON direto!
    db: Session = Depends(get_db)
):
    print("Dados recebidos:", dados.dict(exclude_unset=True))  # Debug
    
    email_existente = db.query(Usuario).filter(Usuario.email == dados.email).first()
    if email_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado!")


    # Verifica se CPF já existe
    usuario_existente = db.query(Usuario).filter(Usuario.cpf == dados.cpf).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="CPF já cadastrado!")
    
    # Cria nova instância do seu model
    novo_usuario = Usuario(
        nome=dados.nome,
        nascimento=dados.nascimento,
        cpf=dados.cpf,
        telefone=dados.tel,
        email=dados.email,
        senha=dados.senha,  # TODO: hash_password(dados.senha)
        cep=dados.cep,
        rua=dados.rua,
        bairro=dados.bairro,
        numero_casa=dados.numero,  # Ajuste campo se necessário
        deficiencia=dados.deficiencia,
        genero=dados.genero
    )
    
    # Salva no banco
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    
    return {
        "message": "Cadastro realizado com sucesso!",
        "id": novo_usuario.id,
        "dados": novo_usuario.__dict__
    }
