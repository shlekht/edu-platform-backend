from groq import Groq
from core.config import settings

groq_client = Groq(api_key=settings.GROQ_API_KEY)
system_prompt = settings.GROQ_SYSTEM_PROMPT