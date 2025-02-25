# Voice Assistant

## Overview

This project is a voice assistant that performs the following steps:
1. Records an audio input for 5 seconds.
2. Transcribes the audio using **OpenAI Whisper**.
3. Sends the transcription to **GPT Chat Completions** for generating a response.
4. Converts the GPT response into speech using **Google gTTS** (Google Text-to-Speech).

The assistant is designed to provide a seamless interaction where users can speak, get a response, and hear it aloud.

---

## Features

- **Audio Recording**: Records audio for 5 seconds using the microphone.
- **Speech-to-Text**: Transcribes the recorded audio using OpenAI's Whisper model.
- **AI-Powered Responses**: Sends the transcription to GPT (e.g., `gpt-3.5-turbo`) to generate a contextual response.
- **Text-to-Speech**: Converts the GPT response into speech using Google's gTTS.
- **Error Handling**: Gracefully handles errors such as API rate limits or transcription failures.

---

## Prerequisites

Before running the project, ensure you have the following:

1. **Python 3.8 or higher** installed.
2. **API Keys**:
   - OpenAI API key for Whisper and GPT.
   - (Optional) Google Cloud API key if using advanced gTTS features.
3. **Libraries**:
   - Install the required Python libraries using the command below.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/voice-assistant.git
   cd voice-assistant
   ```
2. Install the required dependencies
  ```bash
    pip install -r requirements.txt
  ```
3. Setup your environment variables
  - Create a `.env` file in the root directory.
  - Add your OpenAI API Key: 
  ```bash
    OPENAI_API_KEY=your_openai_api_key_here
  ```

## Usage
1. Run the voice assistant
```bash
  python index.py
```

2. Follow the prompts:
 - The assistant will record an audio for 5 seconds (it can be changed at record.py)
 - It will appear `Recording...` at the terminal when starts recording and `Finished Recording` when finished

## Project Structure
```bash
voice-assistant/
├── helpers/
│   ├── whisper_model.py       # Handles audio transcription using Whisper
│   ├── record.py              # Handles audio recording
│   ├── gpt.py                 # Handles GPT chat completions
│   ├── gTTs_mode.py           # Handles text-to-speech using gTTS
├── config/
│   ├── envs.py                # Manages environment variables
├── main.py                    # Main script to run the voice assistant
├── requirements.txt           # List of dependencies
├── README.md                  # Project documentation
```

## Dependencies

The project relies on the following Python libraries:

- **[openai](https://pypi.org/project/openai/)**: For interacting with OpenAI's Whisper and GPT APIs.
- **[gtts](https://pypi.org/project/gtts/)**: For converting text to speech using Google's Text-to-Speech API.
- **[sounddevice](https://pypi.org/project/sounddevice/)**: For recording audio from the microphone.
- **[scipy](https://pypi.org/project/scipy/)**: For saving and processing audio files.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: For managing environment variables (e.g., API keys) stored in a `.env` file.
- **[ipython](https://pypi.org/project/ipython/)**: Optional, for audio playback in Jupyter Notebooks.
- **[playsound](https://pypi.org/project/playsound/)**: Optional, for audio playback in standalone Python scripts.

Install all dependencies using:
```bash
pip install -r requirements.txt