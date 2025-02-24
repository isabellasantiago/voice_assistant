from IPython.display import Audio, display
import sounddevice as sd
from scipy.io.wavfile import write
import os

# To record my audio
def record(seconds=5, sample_rate=44100, output_dir="request_audios"):
  # creates the folder if does not exists
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)

  print("Recording...")
  # Recording the audio
  audio = sd.rec(int(seconds * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
  sd.wait()  # awaits the recording finish
  print("Finished Recording")

  # Define the file name and the file path name
  file_name = 'request_audio.wav'
  file_path = os.path.join(output_dir, file_name)

  # Save the audio in a .wav file
  write(file_path, sample_rate, audio)

  # Returns the full file path name
  return file_path

# Testing implemented function
record_file = record(5)

# Reproduce the recorded audio
display(Audio(record_file, autoplay=True))
