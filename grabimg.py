#!/usr/bin/env python3
# grabimg.py - Grab 10x10px images
import pyautogui
import keyboard
import os

print("Press Ctrl+C to quit")
global i
i = 0
imageDir = 'images/'
imageSize = 15


def deleteLastFile():
    global i
    if i > 0:
        lastFile = imageDir + str(i) + '.png'
        strOut = 'Deleting {:s}'.format(lastFile)
        print(strOut, end='')
        print('\b' * len(strOut), end='', flush=True)
        os.remove(lastFile)
        i-=1
    else:
        print('Have no files')

keyboard.add_hotkey('d', deleteLastFile)


try:
    while True:
        keyboard.wait('s')
        i+=1
        x, y = pyautogui.position()
        fileName = imageDir + str(i)+'.png'
        pyautogui.screenshot(region=(x*2-imageSize/2, y*2-imageSize, imageSize, imageSize)).save(fileName)
        strOut = 'Captured {:s}'.format(fileName)
        print(strOut, end='')
        print('\b' * len(strOut), end='', flush=True)
except KeyboardInterrupt:
    print('\nBye')
