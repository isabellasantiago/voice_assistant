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
    print("Erro: Rate Limit Exceed. Verify plan and billing at OpenAI.")
    return None
  except Exception as e:
    print(f"Error: {e}")
    return None
  
  