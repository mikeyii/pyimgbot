#!/usr/bin/env python3
import keyboard
import pyautogui
from helper import *
import travelling

imageDir = 'images/'
mouseMoveSpeed = 0.75
timingFunction = pyautogui.easeInOutQuad
pyautogui.PAUSE = 1
resourceList = set()


def isMineral():
    return imgExists('images/agat.png') or imgExists('images/aqamarin.png') or imgExists('images/biruza.png')

def isNotCollecting():
    return not imgExists('images/btn_cancel.png')

def isError():
    return imgExists('images/btn_close.png')

def isInBattle():
    return imgExists('images/vs.png')

def isDefeat():
    return imgExists('images/defeat.png')


def click(image):
    coords = findImg(imageDir + image + '.png')
    pyautogui.moveTo(coords[0], coords[1], mouseMoveSpeed, timingFunction)
    pyautogui.click()


def startResourceCollection():
    print('Start collecting')
    pyautogui.click()
    if isError():
        print('Error')
        click('btn_close')
    while len(resourceList):
        x, y = resourceList.pop()
        pyautogui.moveTo(x, y, mouseMoveSpeed, timingFunction)
        pyautogui.click()
        if isMineral():
            print('It is a resource')
            while True:
                pyautogui.doubleClick()
                sleepUntil(isNotCollecting)
                print('Finish collecting')
                if
                if isError():
                    print('Error')
                    click('btn_close')
                elif isInBattle():
                    print('Battle')
                    sleepUntil(isDefeat)
                    click('btn_exit')
                    click('btn_close')
                    click('btn_capital')
                    traveling.travel('Скорбный яр')
                else:
                    break;
        else:
            print('It is not a resource')
    print('Resources finished. Waiting for new resources...')



keyboard.add_hotkey('option', startResourceCollection)


try:
    print('Press commands on each resource')
    while True:
        keyboard.wait('command')
        coords = pyautogui.position()
        resourceList.add(coords)
        print(coords)


except KeyboardInterrupt:
    print('\nBye')
