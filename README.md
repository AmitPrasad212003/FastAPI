# FastAPI

FastAPI is a **modern Python web framework** used to build **REST APIs** quickly with **high performance**, **automatic validation**, and **interactive API docs**.

---

## What is FastAPI?

FastAPI helps you build backend APIs like:

- Login/Signup APIs
- CRUD apps (Todo, Products, Orders)
- Machine Learning model APIs
- Microservices

### Why FastAPI is popular

- **Very fast** (ASGI + async support)
- **Auto validation** using **Pydantic**
- **Auto Swagger docs** at `/docs`
- Easy to write clean, production-style code

---

## Key Terms (FastAPI Ecosystem)

- **Uvicorn**: Server that runs your FastAPI app
- **Pydantic**: Validates request/response data (JSON → Python objects)
- **SQLAlchemy**: Database ORM to interact with DB (SQLite/MySQL/Postgres)

---

## Prerequisites

- Python installed (recommended: Python 3.10+)
- VS Code (optional)
- Terminal / PowerShell

---

## How to Start a New FastAPI Project (Step-by-step)

### Step 1: Create a folder and open terminal inside it

```powershell
mkdir zFastAPI
cd zFastAPI
```

### Step 2: Create virtual environment

```powershell
python-m venv .venv

```

### Step 3: Activate virtual environment

**PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1

```

If PowerShell blocks it:

```powershell
Set-ExecutionPolicy-Scope CurrentUser-ExecutionPolicy RemoteSigned

```

### Step 4: Install FastAPI + Uvicorn

```powershell
pip install fastapi uvicorn

```

### Step 5: Create `main.py`

Create a file named `main.py` and paste:

```python
from fastapiimport FastAPI

app = FastAPI()

@app.get("/")
defroot():
return {"message":"Hello FastAPI"}

```

### Step 6: Run the server

```powershell
uvicorn main:app--reload

```

✅ Server runs at:

- API: `http://127.0.0.1:8000/`
- Docs: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## If the Project Already Exists (How to Start Again)

### Step 1: Go to project folder

```powershell
cd C:\zFastAPI

```

### Step 2: Activate environment

```powershell
.\.venv\Scripts\Activate.ps1

```

### Step 3: Install dependencies (if requirements.txt exists)

```powershell
pip install-r requirements.txt

```

### Step 4: Run project

```powershell
uvicorn main:app--reload

```

---

## Common Commands (Must Know)

### Save installed packages

```powershell
pip freeze > requirements.txt

```

### Install from requirements

```powershell
pip install-r requirements.txt

```

### Deactivate virtual env

```powershell
deactivate

```

### Change port (example 5000)

```powershell
uvicorn main:app--reload--port5000

```

### Run with host (LAN access)

```powershell
uvicorn main:app--reload--host0.0.0.0

```

---

## Real-World Products / Use-cases Using FastAPI

FastAPI is used in real-world for:

- **AI/ML APIs** (serving models)
- **Microservices** in product companies
- **Backend for mobile apps** (authentication + CRUD)
- **Dashboards / Admin panels** backend
- **Payment / Order systems** (as services)

### Examples of real-world style apps built with FastAPI

- **E-commerce backend** (products, cart, orders)
- **Food delivery backend** (restaurants, menu, orders, delivery tracking)
- **Social media backend** (users, posts, likes, comments)
- **Learning platform** (courses, modules, quizzes)
- **Todo / task manager** (CRUD + auth)

> Many startups and teams use FastAPI because it’s fast to develop and easy to scale.
> 

---

## Recommended Production Folder Structure (Optional)

```
app/
  main.py
database.py
  models.py
schemas.py
  routers/
  services/
  core/

```
