from whisper_model import transcribe
from record import record_file

transcription = transcribe(record_file)
print(transcription)