# import cowsay
# import pyttsx3

# engine = pyttsx3.init()
# # this = input("What's this? ")
# # cowsay.cow(this)
# engine.say("hello")
# engine.runAndWait()


from gtts import gTTS
import os

text = input("What's this? ")

from cowsay import cow
print(cow(text))

tts = gTTS(text)
tts.save("output.mp3")

# Play the audio
os.system("mpg321 output.mp3")  # Replace with 'playsound' if needed
