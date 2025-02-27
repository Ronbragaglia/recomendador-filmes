from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class RecommendationRequest(BaseModel):
    user_id: int
    num_recommendations: int


@app.get("/")
def read_root():
    return {"message": "API funcionando corretamente!"}


@app.post("/recommendations/")
def get_recommendations(request: RecommendationRequest):
 
    recommendations = [f"Filme {i+1}" for i in range(request.num_recommendations)]
    return {"user_id": request.user_id, "recommendations": recommendations}


