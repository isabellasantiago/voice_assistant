from helpers.whisper_model import transcribe
from helpers.record import record_file
from helpers.gpt import createChatCompletion
from helpers.gTTs_mode import getVoice

transcription = transcribe(record_file)
print(transcription)

response = createChatCompletion(transcription)

if response is not None:
    print("GPT Answer:", response)
    getVoice(text=response, lang='pt')
else:
    print("Response Error. Ended Proccess.")
