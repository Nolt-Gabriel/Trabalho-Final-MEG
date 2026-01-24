# 🚀 Projeto FastAPI – Tutorial de Instalação

Este documento explica **como instalar, configurar e executar** o projeto desenvolvido com **FastAPI**, de forma simples e direta.

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- 🐍 **Python 3.10 ou superior**
- 🌱 **Git**
- 💻 **Terminal** (Linux/macOS) ou **Prompt / PowerShell** (Windows)

Verifique se o Python está instalado:

```bash
python3 --version
```

---

## 📥 Clonar o repositório

Clone o projeto e entre na pasta:

```bash
git clone <URL_DO_REPOSITORIO>
cd Trabalho-Final-MEG
```

---

## 🧪 Criar o ambiente virtual (venv)

O ambiente virtual serve para isolar as dependências do projeto.

### Linux / macOS
```bash
python3 -m venv venv
```

### Windows
```bash
python -m venv venv
```

---

## ▶️ Ativar o ambiente virtual

### Linux / macOS
```bash
source venv/bin/activate
```

### Windows (PowerShell)
```bash
venv\Scripts\Activate
```

Se aparecer `(venv)` no terminal, o ambiente está ativo ✅

---

## 📦 Instalar as dependências

Com o venv ativado, instale as bibliotecas necessárias:

```bash
pip install fastapi uvicorn sqlalchemy jinja2 python-multipart
```

### 📚 Bibliotecas utilizadas

- **fastapi** → framework backend
- **uvicorn** → servidor ASGI
- **sqlalchemy** → ORM e banco de dados
- **jinja2** → templates HTML dinâmicos
- **python-multipart** → suporte a formulários HTML (`POST`)

---

## 🗄️ Banco de dados

O banco de dados (`database.db`) é criado automaticamente ao rodar o projeto pela primeira vez.

⚠️ Este arquivo **não deve ser enviado ao Git** por motivos de segurança.

---

## 🚀 Executar o projeto

Inicie o servidor com:

```bash
uvicorn main:app --reload
```

Se aparecer algo como:

```
Uvicorn running on http://127.0.0.1:8000
```

o projeto está rodando corretamente 🎉

---

## 🌐 Acessar o site

Abra o navegador e acesse:

```
http://127.0.0.1:8000
```

---

## 🛑 Encerrar o servidor

No terminal, pressione:

```
CTRL + C
```

---

## 🔌 Desativar o ambiente virtual

```bash
deactivate
```

---

## 📁 Estrutura do projeto

```
Trabalho-Final-MEG/
│
├── main.py          # Arquivo principal do FastAPI
├── database.py      # Configuração do banco de dados
├── models.py        # Modelos ORM
├── templates/       # Arquivos HTML
├── static/          # CSS, imagens e JS
├── venv/            # Ambiente virtual (não versionado)
├── .gitignore
└── README.md
```

---

## ✅ Observações importantes

- Sempre ative o **venv** antes de rodar o projeto
- Nunca suba `venv/`, `__pycache__/` ou `database.db` para o Git
- Em outro computador, basta repetir este tutorial

---

📌 *Projeto desenvolvido para fins acadêmicos.*
