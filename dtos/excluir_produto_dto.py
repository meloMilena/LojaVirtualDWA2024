from pydantic import BaseModel, field_validator
from datetime import date, datetime, timedelta

from util.validators import *


class ExcluirProdutoDTO(BaseModel):
    nome: str
    preco: float    
    descricao: str
    estoque: int

