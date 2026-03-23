from fastapi import FastAPI
from app.core.database import SessionLocal

from app.models.usuario import Usuario

app = FastAPI()

@app.get("/")
def root():
    return {"AceWallet no ar!🚀"}

@app.get("/teste-db")
def teste_db():
    db = SessionLocal()
    return {"Teste de conexão com o banco de dados bem-sucedida!"}

# Criação de tabela teste

@app.get("/criar-usuario-teste")
def criar_usuario():
    db = SessionLocal()
    
    novo_usuario = Usuario(
        nome="Usuario",
        sobrenome="Teste",
        cpf="12345678901",
        email="teste@exemplo.com",
        senha="senha123",
        data_nasc="1990-01-01"
    )
    
    db.add(novo_usuario)
    db.commit()
    
    return {"Usuário de teste criado com sucesso!"}

