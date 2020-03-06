from pynput.keyboard import Key
from pynput.mouse import Button
from pynput.keyboard import Controller as key
from pynput.mouse import Controller as Mou
import time

keyboard = key()
mouse = Mou()

def click():
    mouse.position = (376, 747)
    mouse.click(Button.left,1)
    mouse.position = (971, 685)
    mouse.click(Button.left,1)
    for x in open('file.txt'):
         keyboard.type(x)
         keyboard.press(Key.enter)
         time.sleep(1)



if __name__ == "__main__":
     click()
