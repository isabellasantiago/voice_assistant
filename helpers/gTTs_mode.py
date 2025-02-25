from gtts import gTTS
import os
from IPython.display import Audio, display


def getVoice(text, lang):
  output_dir = "response_audios"
  gtts_object = gTTS(
    text=text,
    lang=lang,
    slow=False
  )
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)
  file_name = "response_audio.wav"
  audio_path = os.path.join(output_dir, file_name)
  
  print(audio_path)
  
  gtts_object.save(audio_path)
  display(Audio(audio_path, autoplay=True))