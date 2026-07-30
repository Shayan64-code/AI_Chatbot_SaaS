from fastapi import FastAPI
from routes import chats_routes
from routes import pdf_routes

app = FastAPI()

@app.get("/")
def home():
    return {"message": "This is Home Page."}

app.include_router(chats_routes.router)
app.include_router(pdf_routes.router, prefix="/pdf", tags=["PDF"])
