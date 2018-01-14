#!/usr/bin/env python3
from sys import exit
from pymouse import PyMouse
from pykeyboard import PyKeyboard
# import keyboard
import time
# from PIL import ImageOps
# from numpy import *
# import random
import clipboard

# Game coordinates
coords = {
    'url' :                 (455, 60),
    'duel' :                (641, 494),
    'd50' :                 (864, 456),
    'scoreStart' :          (558, 344),
    'scoreEnd' :            (595, 344),
    'takeCard' :            (602, 377),
    'giveOpponentStep' :    (695, 419),
    'lookOut' :             (720, 535),
    'finish' :              (850, 380),
    'reset' :               (1082, 183),
}

# Init mouse and keyboard
m = PyMouse()
k = PyKeyboard()

btnDisabled = False

def main():
    # keyboard.on_press(keyboardHandler)
    playGame()

def keyboardHandler(ev):
    print(ev.name)
    if ev.name == 's':
        exit()

def playGame():
    time.sleep(1)
    # click Дуэль
    mclick(coords['duel'])
    # click 500 дивных стёкол
    mclick(coords['d50'])
    # take card
    takeCard()
    # Opponent take cards
    time.sleep(.7)
    mclick(coords['giveOpponentStep'])
    # Finish
    time.sleep(.7)
    mclick(coords['finish'])
    # play yet game
    playGame()

def takeCard():
    global btnDisabled
    # Оцениваем
    text = ''
    # Copy
    for i in range(3):
        copy(coords['scoreStart'], coords['scoreEnd'])
        text = clipboard.paste()
        if text != '' :
            print(text)
            break
    print(text)

    # Didn't click look Up
    if text == '':
        copyAllText(coords['url'])
        url = clipboard.paste()
        print(url)
        if len(url) > 31: # http://w2.dwar.mail.ru/main.php

            btnDisabled = True
            closeTab()
            mclick(coords['reset'])
            playGame()
            return
        mclick(coords['lookOut'])
        takeCard()
        return

    # Didn't click finish
    if text == 'абрано':
        if btnDisabled:
            mclick(coords['reset'])
            btnDisabled = False
        else:
            mclick(coords['finish'])
            btnDisabled = True
        playGame()
        return

    # didn't click 500
    if text == 'е сыгр':
        mclick(coords['d50'])
        takeCard()
        mclick(coords['giveOpponentStep'])
        mclick(coords['finish'])
        playGame()
        return

    score = text.split(' ')[0]

    if score.isdigit():
        score = int(score)
        print(score)
        if score < 14:
            print('Take yet card')
            mclick(coords['takeCard'])
            time.sleep(1)
            mclick(coords['lookOut'])
            if score < 12:
                takeCard()
                # take one more card
    else:
    # if another wihdow
        mclick(coords['reset'])
        playGame()
        return

def mclick(coords):
    m.move(coords[0], coords[1])
    time.sleep(.1)
    m.click(coords[0], coords[1])
    time.sleep(.9)

def copyAllText(coords):
    clipboard.copy('')
    mclick(coords)
    time.sleep(.1)
    k.press_key('command')
    time.sleep(.1)
    k.tap_key('a')
    time.sleep(.1)
    k.tap_key('c')
    time.sleep(.1)
    k.release_key('command')

def closeTab():
    k.press_key('command')
    time.sleep(.1)
    k.tap_key('w')
    time.sleep(.1)
    k.release_key('command')

def copy(start, end):
    clipboard.copy('')
    m.release(start[0], start[1])
    time.sleep(.5)
    m.press(start[0], start[1])
    time.sleep(.1)
    m.move(end[0], end[1])
    time.sleep(.1)
    m.release(end[0], end[1])
    time.sleep(.1)
    k.press_key('command')
    time.sleep(.1)
    k.tap_key('c')
    time.sleep(.1)
    k.release_key('command')

if __name__ == '__main__':
    main()
