import requests
import speech_recognition as sr
import pyttsx3 as tts

listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('Specify the city name: ')
engine.runAndWait()

with sr.Microphone() as source:
        print('recording...')
        voice = listener.listen(source)
        city = listener.recognize_google(voice)
        print(city)

engine.say('Displaying Weather report for ' + city)
engine.runAndWait()

url = 'https://wttr.in/{}'.format(city)
result = requests.get(url)

print(result.text)
