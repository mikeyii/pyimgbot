import time
from math import pi, sin, sqrt
import random
import sys
import pyautogui

"""
humanDrag(x, y, button='left')
Drag lika a human

humanMove(x, y)
Move lika a human

"""

# The platformModule is where we reference the platform-specific functions.
if sys.platform.startswith('java'):
    # from . import _pyautogui_java as platformModule
    raise NotImplementedError('Jython is not yet supported by PyAutoGUI.')
elif sys.platform == 'darwin':
    from pyautogui import _pyautogui_osx as platformModule
elif sys.platform == 'win32':
    from pyautogui import _pyautogui_win as platformModule
    from pyautogui_window_win import Window, getWindows, getWindow
else:
    from pyautogui import _pyautogui_x11 as platformModule


MINSPEED = 200
MAXMOUSEMOVE = 700
WIND = 1


class Config:
    """Mouse dynamic config"""
    sinWidthX: 50
    sinWidthY: 50
    sinCountX: 4
    sinCountY: 3



def getPointOnLine(x1, y1, x2, y2, n):
    windX = random.uniform(-WIND, WIND)
    windY = random.uniform(-WIND, WIND)

    generalNoiseK = sin(pi * n)  # 0 = 0, 0.5 = 1, 1 = 1

    sinNoiseX = sin(pi * n * Config.sinCountX)  # 0 0 0.5 = 1 1 = 1
    sinNoiseY = sin(pi * n * Config.sinCountY)  # 0 0 0.5 = 1 1 = 1

    # timing function + sinusoid + small noise
    x  = (x2 - x1) * pyautogui.easeInOutCubic(n) + sinNoiseX * Config.sinWidthX * generalNoiseK + windX * generalNoiseK + x1

    y = (y2 - y1) * pyautogui.easeInOutCubic(n) + sinNoiseY * Config.sinWidthY * generalNoiseK + windY * generalNoiseK + y1

    return (x, y)


def move(x, y, pause=None, _pause=True):
    """Move mouse like a human"""
    x, y = pyautogui._unpackXY(x, y)
    pyautogui._failSafeCheck()
    _humanMoveDrag('move', x, y)
    pyautogui._autoPause(pause, _pause)


def drag(x, y, button='left', pause=None, _pause=True):
    """Drag mouse like a human"""
    pyautogui._failSafeCheck()
    x, y = pyautogui._unpackXY(x, y)
    pyautogui.mouseDown(button=button, _pause=False)
    _humanMoveDrag('drag', x, y, button)
    pyautogui.mouseUp(button=button, _pause=False)
    pyautogui._autoPause(pause, _pause)


def _humanMoveDrag(moveOrDrag, x, y, button='left'):
    if sys.platform != 'darwin':
        moveOrDrag = 'move'  # Only OS X needs the drag event specifically.

    if x is None and y is None:
        return  # Special case for no mouse movement at all.

    startx, starty = pyautogui.position()

    x = int(x) if x is not None else startx
    y = int(y) if y is not None else starty

    width, height = pyautogui.size()

    # Make sure x and y are within the screen bounds.
    x = max(0, min(x, width - 1))
    y = max(0, min(y, height - 1))

    # If the duration is small enough, just move the cursor there instantly.
    steps = [(x, y)]

    dx = x - startx
    dy = y - starty
    distance = sqrt(dx*dx + dy*dy)

    # generate speed
    speed = MINSPEED + ((distance / 30) ** 2) * random.uniform(0.8, 1.2)

    duration = distance / speed

    if distance > MAXMOUSEMOVE and moveOrDrag is not 'drag':
        part = random.uniform(0.35, 0.65)
        randomOffsetX = random.uniform(-70, 89)
        randomOffsetY = random.uniform(-56, 62)
        _humanMoveDrag(moveOrDrag,
                       startx + dx * part + randomOffsetX,
                       starty + dy * part + randomOffsetY)
        _humanMoveDrag(moveOrDrag, x, y)
        return

    if duration > pyautogui.MINIMUM_DURATION:
        # Non-instant moving/dragging involves tweening:
        # num_steps = max(width, height)
        num_steps = int(max(1.0, duration * 120.0))
        sleep_amount = duration / num_steps
        if sleep_amount < pyautogui.MINIMUM_SLEEP:
            num_steps = int(duration / pyautogui.MINIMUM_SLEEP)
            sleep_amount = duration / num_steps

        # generate sin config
        Config.sinCountX = random.randint(1, 4)
        Config.sinCountY = random.randint(1, 3)
        Config.sinWidthX = random.uniform((-dx - 40) / 20, (dx + 40) / 20)
        Config.sinWidthY = random.uniform((-dx - 40) / 20, (dx + 40) / 20)

        steps = [
            getPointOnLine(startx, starty, x, y, n / num_steps)
            for n in range(num_steps)
        ]
        # Making sure the last position is the actual destination.
        steps.append((x, y))

        for tweenX, tweenY in steps:
            if len(steps) > 1:
                # A single step does not require tweening.
                time.sleep(sleep_amount)

            pyautogui._failSafeCheck()
            if moveOrDrag == 'move':
                platformModule._moveTo(tweenX, tweenY)
            elif moveOrDrag == 'drag':
                platformModule._dragTo(tweenX, tweenY, 'left')
            else:
                raise NotImplementedError('Unknown value of moveOrDrag: {0}'.format(moveOrDrag))
            time.sleep(sleep_amount)

        pyautogui._failSafeCheck()
