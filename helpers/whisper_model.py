import whisper

language = 'pt'
model = whisper.load_model('medium')

def transcribe(audio):
  transcription = model.transcribe(audio, fp16=False, language=language)
  return transcription['text']
