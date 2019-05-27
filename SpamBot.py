import random
import pyautogui
import sys
import time
import win32api, win32com

SpamText = ['Nerd', 'I Hate You', 'NOOB', 'Get Cancer', 'U fuck lol', 'Hi', 'Spotlight', 'Moonlight', 'Dont smoke weed smoke JESUS',  'FBI DONT FCKING MOVE!', 'LOL', 'You seem nice. Its a shame that I have to kill you.', 'DIE, DIE, DIE', "HAMMER DOWN!", "I'VE GOT YOU IN MY SIGHTS", "NIGGA U GAY", 'I like trains', 'ITS TIME TO STAPH!', 'I need healing.']
mposx = 0
mposy = 0

def spam():
    endcount = eval(input('Inserire la quantità di messaggi da inviare: '))
    print("Clicca quando sei pronto.")
    state_left = win32api.GetKeyState(0x01)
    mousePressed = False
    while mousePressed == False:
        a = win32api.GetKeyState(0x01)
        if a != state_left:
            mousePressed = True
            mposx, mposy = pyautogui.position()
        time.sleep(.01)
    count = 1
    while count <= endcount:
        state_esc = win32api.GetKeyState(0x1B)
        if state_esc > 0:
            break
        pyautogui.click(mposx, mposy)
        pyautogui.typewrite(random.choice(SpamText), interval=0.01)
        pyautogui.hotkey('enter')
        count += 1

def singleSpam(userPhrase):
    endcount = eval(input('Inserire la quantità di messaggi da inviare: '))
    print("Clicca quando sei pronto.")
    state_left = win32api.GetKeyState(0x01)
    mousePressed = False
    while mousePressed == False:
        a = win32api.GetKeyState(0x01)
        if a != state_left:
            mousePressed = True
            mposx, mposy = pyautogui.position()
        time.sleep(.01)
    count = 1
    while count <= endcount:
        state_esc = win32api.GetKeyState(0x1B)
        if state_esc > 0:
            break
        pyautogui.click(mposx, mposy)
        pyautogui.typewrite(userPhrase, interval=0.01)
        pyautogui.hotkey('enter')
        count += 1

def gather():
    sPhrase = eval(input('(1)Inserisci una frase personalizzata, o (2)una frase già pronta: '))
    if sPhrase == 1:
        userPhrase = input('Inserisci una frase che vorresti inviare: ')
        singleSpam(userPhrase)
        print('Spam terminato')
    elif sPhrase == 2:
        spam()
        print('Spamm frase già pronta')
    else:
        print('Selezione non valida. Riprova.')
        gather()

gather()
