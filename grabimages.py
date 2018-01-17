#!/usr/bin/env python3
# grabimages.py - grab images and save them with name
import pyautogui as gui

imageDir = 'images/';


def saveImage(size=10):
    x, y = gui.position()
    im = gui.screenshot(region=(x*2 - size/2, y*2 - size/2, size, size))
    print(x, y)
    result = tuple(gui.locateAllOnScreen(im, grayscale=True))
    im.show()
    print("Found {}", len(result))
    save = input('Do you want to save? ')
    if save == 'y':
        name = input('Write name for that image: ')
        im.save(imageDir + name + '.png')

def main():
    print('Press Ctrl+C to exit')
    try:
        while True:
            input('Press Enter to save image')
            # Blocks until you press esc.
            saveImage()
    except KeyboardInterrupt:
        print('\nDone.')


if __name__ == "__main__":
    main()
