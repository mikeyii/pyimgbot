import pyautogui
from time import sleep
import random

retina = True
mouseMoveSpeed = (0.4, 0.8)
timingFunction = pyautogui.easeInOutQuad
pyautogui.PAUSE = .93
imageDir = 'images/'



def fixRetina(coords):
    if retina and coords:
        x, y = coords
        x = x / 2
        y = y / 2
        return x, y
    return coords

def findImg(img):
    return fixRetina(pyautogui.locateCenterOnScreen('images/' + img + '.png', grayscale=True))

def imgExists(img):
    if isinstance(img, str):
        return bool(pyautogui.locateOnScreen('images/' + img + '.png', grayscale=True))
    else:
        for i in img:
            if pyautogui.locateOnScreen('images/' + i + '.png', grayscale=True):
                return True
        return False

def sleepUntilImg(img):
    coords = imgExists(img)
    while not coords:
        sleep(pyautogui.PAUSE)
        coords = findImg(img)
    return findImg(img)

def sleepWhileImg(img):
    while imgExists(img):
        sleep(pyautogui.PAUSE)
    return findImg(img)

def niceMove(x=None, y=None):
    if isinstance(x, str):
        coords = findImg(x)
        if coords:
            x, y = coords
        else:
            print('Image', x, 'not found')
            return
    r1, r2 = mouseMoveSpeed
    print('move to', x, y)
    pyautogui.moveTo(x, y, random.uniform(r1, r2), timingFunction)


def niceClick(x=None, y=None, waiting=0):
    if isinstance(x, tuple):
        waiting = y
        x, y = x
    if isinstance(x, str):
        coords = findImg(x)
        if coords:
            x, y = coords
        else:
            print('Image', x, 'not found')
            return
    pos = pyautogui.position()
    if (x or y) and (x != pos[0] or y != pos[1]):
        niceMove(x, y) # First move to dirrection
    pyautogui.click()
    print('click', x, y)
    if waiting:
        sleep(waiting)

def waitClick(img):
    sleepUntilImg(img)
    niceClick(img)
