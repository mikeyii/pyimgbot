import pyautogui
from time import sleep
import random
from math import floor, sqrt # for retina fix images

from humanmouse import humanMove

retina = True
pyautogui.PAUSE = .93
imageDir        = 'images/'



def clickArea(img, size):
    coords = findImg(img)
    if not coords:
        print('Image not found')
        return
    x, y = coords
    return random.uniform(x - size, x + size) ,random.uniform(y - size, y + size)





def screenshot(region = None):
    return pyautogui.screenshot(region=region)

def checkPixel(x, y, color):
    return pyautogui.pixelMatchesColor(x, y, color)

def niceDrag(x, y = None):
    if isinstance(x, tuple):
        x, y = x
    pyautogui.mouseDown()
    humanMove(x, y)
    pyautogui.mouseUp()

def findAllPixels(pixel, im, distance = 5, draw = False):
    result = []
    prev = (0, 0)
    for x in range(im.width):
        for y in range(im.height):
            if im.getpixel((x, y)) == pixel:
                if x - prev[0] < distance and y - prev[1] < distance:
                    continue
                print(x, y)
                result.append((x, y))
                prev = (x, y)
    return result

def fixRetina(coords):
    if retina and coords:
        x, y = coords
        x = floor(x / 2)
        y = floor(y / 2)
        return x, y
    return coords

def findImg(img):
    """
    return list(int, int) or None
    """
    return fixRetina(pyautogui.locateCenterOnScreen('images/' + img + '.png', grayscale=True))

def imgExists(img):
    """
    return bool
    """
    return bool(pyautogui.locateOnScreen('images/' + img + '.png', grayscale=True))

def anyImgExists(images):
    """
    return bool
    """
    for img in images:
        if imgExists(img):
            return True
    return False

def sleepUntilImg(img):
    """
    return list(int, int), sleep until image will be on screen
    """
    coords = findImg(img)
    while not coords:
        sleep(pyautogui.PAUSE)
        coords = findImg(img)
    return coords

def sleepWhileImg(img):
    """
    return None, sleep while image on screen
    """
    while imgExists(img):
        sleep(pyautogui.PAUSE)

def sleepWhileImages(img):
    """
    return None, sleep while image on screen
    """
    while anyImgExists(img):
        sleep(pyautogui.PAUSE)

def niceMove(x=None, y=None, waiting=0):
    """
    return None move mouse to current position
    x = None, truple, str, int
    y = None, int
    """
    if isinstance(x, str):
        coords = findImg(x)
        if not coords:
            print('Image', x, 'not found')
            return
        else:
            waiting = y
            x, y = coords

    if isinstance(x, tuple):
        waiting = y
        x, y = x
    print('move to', x, y, waiting)
    humanMove(x, y)
    if waiting:
        sleep(waiting)


def niceClick(x=None, y=None, waiting=0, clicks=1, size = 0, area = ()):
    """
    return None move mouse to current position
    x = None, truple, str, int
    y = None, int
    """
    if isinstance(x, tuple):
        waiting = y
        x, y = x
    if isinstance(x, str):
        coords = findImg(x)
        if coords:
            waiting = y
            x, y = coords
        else:
            print('Image', x, 'not found')
            return
    pos = pyautogui.position()
    print(x, y)
    if (x or y) and (x != pos[0] or y != pos[1]):
        print(size)
        if size > 0:
            x, y = random.uniform(x - size, x + size), random.uniform(y - size, y + size)
            print('New x y')
            print(x, y)
        elif area:
            x, y = random.uniform(x + area[0], x + area[2]), random.uniform(y + area[1], y + area[3])
        niceMove(x, y) # First move to dirrection
        sleep(.5)
    print('click', x, y, waiting)
    pyautogui.click(clicks = clicks)
    if waiting:
        sleep(waiting)

def waitClick(img, size=0, area=()):
    coords = sleepUntilImg(img)
    niceClick(coords, size, area)
