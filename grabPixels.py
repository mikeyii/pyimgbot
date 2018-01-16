#!/usr/bin/env python3
# grabpixels.py - grab pixels and save them with name

from pymouse import PyMouse
from PIL import ImageDraw, ImageGrab

m = PyMouse()
infoStopped = False


def savePixel():
    infoStopped = True
    x, y = m.position()
    im = ImageGrab.grab()
    pixel = im.getpixel((x*2, y*2))
    pixelStr = '({}, {}, {}, {}),'.format(pixel[0], pixel[1], pixel[2], pixel[3])
    distance = input('Enter distance(5):')
    if distance == '':
        distance = 5
    else:
        distance = int(distance)
    result = generateImage(pixel, im, distance)
    print('Catched ', len(result))
    im.save('1.png')
    im.show()
    save = input('Do you want to save? ')
    if save == 'y':
        name = input('Write name for that pixel: ')
        pixelStr = '"{}": '.format(name) + '{"pixel":' +  pixelStr + '"distance": ' + distance + '},\n'
        with open("grabPixels.txt", "a") as myfile:
                myfile.write(pixelStr)


def generateImage(pixel, im, distance = 5):
    draw = ImageDraw.Draw(im)
    result = []
    prev = (0, 0)
    for x in range(im.width):
        for y in range(im.height):
            if im.getpixel((x, y)) == pixel:
                if x - prev[0] < distance and y - prev[1] < distance:
                    continue
                # print(x, y)
                draw.ellipse((x - 20, y - 20, x + 20, y + 20), outline='red')
                result.append((x, y))
                prev = (x, y)
    return result

try:
    while True:
        input('Press Enter to save pixel')
        # Blocks until you press esc.
        savePixel()
except KeyboardInterrupt:
    print('\nDone.')
