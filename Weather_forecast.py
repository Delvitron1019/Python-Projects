import requests
import pyttsx3 as tts

engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

city = input('Enter the city name: ')
engine.say('Displaying Weather report for ' + city)
engine.runAndWait()
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)
print(res.text)