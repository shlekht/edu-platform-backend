from fastapi import APIRouter, HTTPException
from schemas.chat import MessageInSchema, MessageOutSchema
from services import chat_service

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=MessageOutSchema)
def generate_llm_response(
    message_in: MessageInSchema
): 
    try:
        llm_response = chat_service.generate_llm_response(message_in.text)
        return {"text": llm_response}
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )