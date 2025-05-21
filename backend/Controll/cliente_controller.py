from fastapi import APIRouter
from fastapi.responses import JSONResponse
from backend.Service import cliente_service
from pydantic import BaseModel
from backend.Model.cliente_model import Cliente

# Criando o roteador
router = APIRouter()

# POST /avaliar
@router.post("/avaliar")
async def avaliacao(cliente: Cliente):
    print(f"Iniciando a avaliação: {cliente}")
    r = cliente_service.calc_nucleo(Cliente)
    print(f"Resultado: {r.resposta}")
    return JSONResponse(content=r.dict())

# GET /health
@router.get("/health")
def read_health():
    return {"status": "funcionando"}
