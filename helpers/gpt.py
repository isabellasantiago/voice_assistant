from openai import OpenAI, RateLimitError
from config.envs import openai_key

client = OpenAI(api_key=openai_key)

def createChatCompletion(transcription):
  try:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{
        "role": "user",
        "content": transcription
      }]
    )
    return response.choices[0].message.content
  except RateLimitError:
    print(f"Erro: Limite de cota excedido. Verifique seu plano e billing na OpenAI.")
  except Exception as e:
    print(f"Erro inesperado: {e}")
  
  