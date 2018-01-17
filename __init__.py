import pyautogui
from math import floor
import random
import time
from . import humanmouse
import clipboard

imageDir = 'images/'

retina = True

# Images part

def _fixRetina(coords):
    if retina and coords:
        x, y = coords
        x = floor(x / 2)
        y = floor(y / 2)
        return x, y
    return coords


def imgExists(img):
    return bool(pyautogui.locateOnScreen(imageDir + img + '.png', grayscale=True))

def findImg(img, exception=True):
    coords = _fixRetina(pyautogui.locateCenterOnScreen(imageDir + img + '.png', grayscale=True))
    if not coords and exception:
        print('Image \'{}\' not found'.format(img))
    else:
        return coords

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
        time.sleep(pyautogui.PAUSE)
        coords = findImg(img)
    return coords

def sleepWhileImg(img):
    """
    Sleep while image on screen
    """
    while imgExists(img):
        time.sleep(pyautogui.PAUSE)

def sleepWhileAnyImg(img):
    """
    Sleep while any images on screen
    """
    while anyImgExists(img):
        time.sleep(pyautogui.PAUSE)


def findAllPixels(pixel, im, mindistance = 5):
    result = []
    prev = (0, 0)
    for x in range(im.width):
        for y in range(im.height):
            if im.getpixel((x, y)) == pixel:
                if x - prev[0] < mindistance and y - prev[1] < mindistance:
                    continue
                print(x, y)
                result.append((x, y))
                prev = (x, y)
    return result

def grab(region=None, mouse=False, size=5):
    if (mouse):
        x, y = pyautogui.position()
        region = (x-size, y-size, x+size, y+size)
    return pyautogui.screenshot(region=region)

# Ended images part

# Mouse part

def _unpackXYPause(x, y=None, pause=None):
    if isinstance(x, tuple):
        return x[0], x[1], y
    else:
        return x, y, pause

def move(x, y=None, pause=None, size=0, area=()):
    if isinstance(x, str):
        x, y, pause = _unpackXYPause(findImg(x), y)
    else:
        x, y, pause = _unpackXYPause(x, y, pause)  # for use move('images', 3) when 3 is pause

    if x is None and y is None:
        if pause:
            time.sleep(pause)
        return

    if size:
        x = random.randint(x-size, x+size)
        y = random.randint(y-size, y+size)

    if area:
        x = random.randint(x-area[0], x+area[2])
        y = random.randint(y-area[1], y+area[3])

    # move
    humanmouse.move(x, y, pause)


def click(x, y=None, pause=None, clicks=1, size=0, area=()):
    # move pause = None, because that's click pause
    move(x, y, size=size, area=area)

    pyautogui.click(pause=pause, clicks=1)


def waitClick(image, size=0, area=()):
    coords = sleepUntilImg(image)
    click(coords, size, area)


# Keyboard part

def typeToImg(image, string, size, area=(), utf=False):
    if (imgExists(image)):
        click(image)
        if not utf:
            clipboard.copy(string)
            pyautogui.hotkey('command', 'v')
        else:
            pyautogui.typewrite(string, interval=0.05)
        return
    print('Image \'{}\' not found'.format(image))
