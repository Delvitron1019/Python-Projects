import smtplib
import speech_recognition as sr
import pyttsx3 as tts
from email.message import EmailMessage

listener = sr.Recognizer()
engine = tts.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('recording...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, body, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('dnts5203@gmail.com', 'pngarmghzkixbwnb')
    email = EmailMessage()
    email['From'] = 'dnts5203@gmail.com'
    email['To'] = receiver
    email['Subject'] = body
    email.set_content(message)
    server.send_message(email)

def get_email_info():
    receiver = input('To whom do you wish to send this mail? \n')
    talk('What is the subject of your email?')
    body = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, body, message)
    talk('Email sent successfully!')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    else:
        talk('Ok! Have a good day.')

get_email_info()