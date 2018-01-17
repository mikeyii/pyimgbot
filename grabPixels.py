#!/usr/bin/env python3
# grabpixels.py - grab pixels and save them with name

from pymouse import PyMouse
from PIL import ImageDraw, ImageGrab
from string import Template

m = PyMouse()
retina = True

def isYes(value):
    return value.lower() in ('y', 'yes')

def savePixel():
    x, y = m.position()
    im = ImageGrab.grab()
    if retina:
        x = x * 2
        y = y * 2
    pixel = im.getpixel((x, y))
    pixelStr = '({}, {}, {}, {})'.format(pixel[0], pixel[1], pixel[2], pixel[3])
    changeDistance = 'y'
    while isYes(changeDistance):
        distance = input('Enter distance(5):')
        if distance == '':
            distance = 5
        else:
            distance = int(distance)
        result = generateImage(pixel, im, distance)
        print('Catched ', len(result))
        im.show()
        save = input('Do you want to save it?(y): ') or 'y'
        if isYes(save):
            name = input('Write name for that pixel: ')
            s = Template('"$name": {"pixelcolor": $pixel, "distance": $distance},\n')
            with open("grabPixels.txt", "a") as myfile:
                myfile.write(s.substitute(name=name, pixel=pixelStr, distance=distance))
            changeDistance = 'n'

        else:
            changeDistance = input('Do you want to changeDistance?(n): ')


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


def main():
    print('Press Ctrl+C to exit')
    try:
        while True:
            input('Press Enter to save pixel')
            # Blocks until you press esc.
            savePixel()
    except KeyboardInterrupt:
        print('\nDone.')


if __name__ == "__main__":
    main()
