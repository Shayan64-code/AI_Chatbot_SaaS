from fastapi import APIRouter
from schemas import chat_schemas
from services import ai_services as cb

router = APIRouter()

@router.post("/chat", response_model= chat_schemas.ChatResponse)
async def chat_endpoint(request : chat_schemas.ChatRequest):
    response = cb.chatbot(request.message)
    return chat_schemas.ChatResponse(reply= response["message"])
