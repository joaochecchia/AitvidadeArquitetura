# Exemplo de modelo Pydantic para o cliente
class Cliente(BaseModel):
    nome: str
    idade: int
    # adicione outros campos necessários