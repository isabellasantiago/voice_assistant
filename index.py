from helpers.whisper_model import transcribe
from helpers.record import record_file
from helpers.gpt import createChatCompletion

transcription = transcribe(record_file)
print(transcription)

response = createChatCompletion(transcription)
print(response)
