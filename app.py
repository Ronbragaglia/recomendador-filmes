from fastapi import FastAPI
from pydantic import BaseModel

# Criando a instância da API
app = FastAPI()

# Estrutura esperada para a requisição
class RecommendationRequest(BaseModel):
    user_id: int
    num_recommendations: int

# Rota principal de teste
@app.get("/")
def read_root():
    return {"message": "API funcionando corretamente!"}

# Rota para recomendações de filmes
@app.post("/recommendations/")
def get_recommendations(request: RecommendationRequest):
    # Simulação de recomendação (substitua pela lógica real)
    recommendations = [f"Filme {i+1}" for i in range(request.num_recommendations)]
    return {"user_id": request.user_id, "recommendations": recommendations}


