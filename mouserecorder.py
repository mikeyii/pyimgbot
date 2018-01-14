#!/usr/bin/env python3
# grabimg.py - Record resource position
import pyautogui
import keyboard
import time

print("Press Ctrl+C to quit")

resourceList = set()

retina = True

def isResourceSelected():
    # Agat
    return pyautogui.pixelMatchesColor(2092, 264, (179, 211, 209))

def isError():
    return pyautogui.pixelMatchesColor(1394, 352, (250, 223, 189))

def isDead():
    return pyautogui.pixelMatchesColor(1508, 552, (185, 158, 119))

def isInBattle():
    return pyautogui.pixelMatchesColor(428, 210, (92, 110, 31))

def isBattleFinished():
    return pyautogui.pixelMatchesColor(996, 610, (157, 30, 20))

def isBattleStatistic():
    return pyautogui.pixelMatchesColor(1442, 444, (251, 237, 197)

def startResourceCollection():
    pyautogui.click()
    while len(resourceList):
        x, y = resourceList.pop()
        pyautogui.click(x, y)
        if isResource():
            print('It is a resource')
            while True:
                pyautogui.doubleClick(x, y)
                time.sleep(21)
                if isError():
                    pyautogui.click(700, 235)
                else:
                    break
        else:
            print('It is not a resource')
    print('Resources finished. Waiting for new resources...')

keyboard.add_hotkey('d', startResourceCollection)

try:
    while True:
        keyboard.wait('s')
        coords = pyautogui.position()
        resourceList.add(coords)
        print(coords)

except KeyboardInterrupt:
    print('\nBye')
