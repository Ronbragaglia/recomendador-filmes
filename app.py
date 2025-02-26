from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API funcionando corretamente!"}

git add app.py
git commit -m "Corrigindo erro de ASGI no FastAPI"
git push origin main
