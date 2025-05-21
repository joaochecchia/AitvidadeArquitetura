from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
import joblib

from backend.Controll import cliente_controller 
from utils import jsonc
from models import Cliente, Resposta 

# Carrega o modelo
modelo = joblib.load('modelo_cluster_cartao_credito.pkl')

# Cria a instância do FastAPI
app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(cliente_controller.router)

# Execução (caso rode como script diretamente)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
