import os

from gtts import gTTS       # we have imported this module for text to speech conversion

text = "hello guys. how are you. all fine"
language = 'en'   # en is for english language
obj = gTTS(text=text, lang=language, slow=False)
# we have used slow = False because our converted video will have a high speed
obj.save("sample.mp3")

# to open the video fle automatically we have to import os
os.system("sample.mp3")