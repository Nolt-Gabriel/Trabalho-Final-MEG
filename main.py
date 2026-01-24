from fastapi import FastAPI, Form, Request, Cookie
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# ROTA PRINCIPAL (/)
@app.get("/")
def home(request: Request, usuario: str | None = Cookie(None)):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "logado": usuario is not None,
            "usuario": usuario
        }
    )


# LOGIN (recebe formulário)
@app.post("/login")
def login(email: str = Form(...), senha: str = Form(...)):
    # AQUI entraria a validação no banco
    # (vamos fingir que sempre dá certo)

    response = RedirectResponse("/", status_code=302)
    response.set_cookie(key="usuario", value=email)
    
    return response


# LOGOUT
@app.get("/logout")
def logout():
    response = RedirectResponse("/", status_code=302)
    response.delete_cookie("usuario")
    return response