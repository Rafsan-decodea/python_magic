import speech_recognition as sr
from pynput.keyboard import Controller as key_controller
from pynput.keyboard import Key
import time

voice = sr.Recognizer()
keyboard = key_controller()

def writter():
    with sr.Microphone() as sourch:
        print ('listening.....')
        data = voice.listen(sourch)
        data_final = voice.recognize_google(sourch)
        print ('now Typing.....')
        for x in data_final:
             keyboard.type(x)
             time.sleep(0.1)
        keyboard.press(Key.enter)
    writter()

if __name__ == '__main__':
    writter()