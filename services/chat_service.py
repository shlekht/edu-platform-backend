from core.groq_client import groq_client, system_prompt
import re

def generate_llm_response(prompt: str):
    
    chat_completion = groq_client.chat.completions.create(
        messages=[
            
            {
                "role": "system",
                "content": system_prompt
            },
            
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="qwen/qwen3-32b"
    )
    
    result = chat_completion.choices[0].message.content or ""
    clean_response = re.sub(r'<think>.*?</think>', '', result, flags=re.DOTALL).strip()
    return  clean_response