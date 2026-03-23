from fastapi import FastAPI
from app.core.database import SessionLocal

app = FastAPI()

@app.get("/")
def root():
    return {"AceWallet no ar!🚀"}

@app.get("/teste-db")
def teste_db():
    db = SessionLocal()
    return {"Teste de conexão com o banco de dados bem-sucedida!"}