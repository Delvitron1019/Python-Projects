import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit
import pyjokes
import wikipedia
import python_weather as pw

weather = pw.Client(format=pw.IMPERIAL)
listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def activate_jay():
    with sr.Microphone() as source:
            print('recording...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'j' in command:
                command = command.replace('jay ', '')
                talk('Request received.')
    
    if 'play' in command:
        song = command.replace('play ', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    if 'hear' in command:
        song = command.replace('I want to hear ', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        talk('Here is a joke for you.')
        talk(pyjokes.get_joke())
    elif 'who are you' in command:
        talk('I am a virtual assistant of Dev Shah.')
    elif 'who' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'what' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'how is weather in' in command:
        city = command.replace('how is weather in ','')
        talk(weather(city))
    elif 'what is weather of' in command:
        city = command.replace('what is weather of ','')
        talk(weather(city))
        print(weather(city))
    else:
        talk('Pardon?')
        activate_jay()

talk('Jarvis is ready to comply')
activate_jay()