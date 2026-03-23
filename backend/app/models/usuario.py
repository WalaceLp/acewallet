from sqlalchemy import Column, String, Date, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.models.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String(100), nullable=False)
    sobrenome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    senha = Column(String, nullable=False)
    data_nasc = Column(Date, nullable=False)
    criado_em = Column(TIMESTAMP, server_default=func.now())
    atualizado_em = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())