from fastapi import FastAPI, Form, Request, Cookie
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import SessionLocal, engine
from models import Base, Usuario

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)

# ROTA PRINCIPAL (/)
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


# LOGIN (recebe formulário)
@app.post("/login")
def login(email: str = Form(...), senha: str = Form(...)):
    # Aqui entra a validação no banco

  db = SessionLocal()
  
  #Procura no banco o email digitado
  usuario = db.query(Usuario).filter(Usuario.email == email).first()

  db.close()

  #Se nao for um usuario no banco, ou a senha for diferente o login esta errado
  if not usuario or usuario.senha != senha:
      return RedirectResponse("/", status_code=302)

  response = RedirectResponse("/", status_code=302)
  response.set_cookie(key="usuario", value=email)
  
  return response



@app.post("/cadastro")
def cadastro(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    telefone: str = Form(...)
):
    db = SessionLocal()

    # Verifica se o email já existe
    usuario_existente = db.query(Usuario).filter(Usuario.email == email).first()

    if usuario_existente:
        db.close()
        return templates.TemplateResponse(
            "home.html",
            {
                "request": request,
                "erro": "Este email já está cadastrado.",
            }
        )
        #return RedirectResponse("/", status_code=302)

    # Cria novo usuário
    novo_usuario = Usuario(
        nome=nome,
        email=email,
        senha=senha,
        telefone=telefone
    )

    db.add(novo_usuario)
    db.commit()
    db.close()

    # (opcional) já loga o usuário após cadastro
    response = RedirectResponse("/", status_code=302)
    response.set_cookie(key="usuario", value=email)

    return response 


# LOGOUT
#@app.get("/logout")
#def logout():
#    response = RedirectResponse("/", status_code=302)
#    response.delete_cookie("usuario")
#    return response