import pygame
from gtts import gTTS
from io import BytesIO
import pyttsx3



def play_audio(text):
  try:
      tts = gTTS(text=text, lang='es')
      speech_bytes = BytesIO()
      tts.write_to_fp(speech_bytes)
      speech_bytes.seek(0)
      pygame.mixer.init()
      pygame.mixer.music.load(speech_bytes)
      pygame.mixer.music.play()
      while pygame.mixer.music.get_busy():
          continue
  except Exception:
      print("Usando pyttsx3 en su lugar...")
      engine = pyttsx3.init()
      engine.say(text)
      engine.runAndWait()


