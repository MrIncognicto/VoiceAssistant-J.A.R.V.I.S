from gtts import gTTS
import os
from playsound import playsound
import random
import time

def speak(text):
    tts=gTTS(text,lang='en',slow=False)
    tts.save('hey.mp3')
    playsound('hey.mp3')
    time.sleep(3)
    os.remove('hey.mp3')


speak('Hello Everyone and welcome back')
