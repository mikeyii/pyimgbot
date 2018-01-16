#!/usr/bin/env python3
# mouseNow.py - Displays the mouse cursor's current position
from PIL import ImageGrab
from pymouse import PyMouse
print("Press Ctrl+C to quit")

retina = 2
m = PyMouse()

try:
    while True:
        # Get and print mouse coordinates
        x, y = m.position()
        positionStr = 'X: {:4} Y: {:4}'.format(round(x), round(y))
        # pixelColor = ImageGrab.grab().getpixel((x*2, y*2))
        # positionStr += ' RGB: ({:s}, {:s}, {:s})'.format(str(pixelColor[0]).rjust(3), str(pixelColor[1]).rjust(3), str(pixelColor[2]).rjust(3))

        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')
