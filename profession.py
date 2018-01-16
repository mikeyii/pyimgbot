#!/usr/bin/env python3
from helper import *
import travelling
from huntmap import HuntMap
from PIL import Image, ImageDraw

shade = 0.7

resources = {
    "Агат": (104, 149, 226, 255),
    "Аквамарин": (133, 207, 187, 255),
    "Бирюза": (177, 104, 110, 255),
}

def isResource():
    return imgExists('agat.png')



# Start
location = input('Введите лоакцию: ')
resource = input('Введите ресурс: ')
if location:
    travelling.travel(location)
    niceClick('hunt', 3, size=5)
# Find hunt area
coords = findImg('hunt_top_left')
xOffset, yOffset = findImg('hunt_top_left')
width, height = findImg('hunt_bottom_right')
area = (xOffset * 2, yOffset * 2, width * 2 - xOffset * 2, height * 2 - yOffset * 2)
startCollect()
# Capturing

def startCollect(resource):
    huntMap = HuntMap()
    while True:
        print('Capturing screen');
        im = pyautogui.screenshot(region=area)
        resourcesCoords = findAllPixels(resources[resource], im)
        while len(resourcesCoords) == 0:
            niceClick(huntMap.getRandomCoords(), size=5)
            im = pyautogui.screenshot(region=area)
            resourcesCoords = findAllPixels(resources[resource], im)
        for coords in resourcesCoords:
            x, y = coords
            xCoord = (x + xOffset * 2) / 2
            yCoord = (y + yOffset * 2) / 2
            print(xCoord, yCoord)
            if checkPixel(xCoord * 2, yCoord * 2, resources[resource]):
                niceClick(xCoord, yCoord, 3, clicks=2, size=4)
                print('Собираем ресурс')
                # niceClick(xCoord, yCoord)
                # if imgExists('collect_mineral'):
                #     niceClick('collect_mineral')
                sleepWhileImg('labels/first_collect')
                print('Didnt find label first collect')
                if imgExists('btn/cancel'):
                    niceClick('btn/cancel', size=3)
                while imgExists('btn/close'):
                    niceClick('btn/close', size=3)
                    if checkPixel(xCoord * 2, yCoord * 2, resources[resource]):
                        niceClick(xCoord, yCoord, 3, clicks=2, size=4)
                        sleepWhileImg('labels/first_collect')
                        # niceClick(xCoord, yCoord)
                        # if imgExists('collect_mineral'):
                        #     niceClick('collect_mineral')
                while imgExists('vs'):
                    print('We are in the battle')
                    battle()
                    travelling.travel(location)
                while imgExists('labels/capcha'):
                    capcha()
                if imgExists('labels/no_instrument'):
                    print('Заноза!')
                    exit()
                print('Iteration finished')


def battle():
    waitClick('btn/exit', size=3)
    waitClick('btn/in_location', size=3)
    waitClick('btn/capital', size=3)

def capcha():
    capchaCoords = [
        findImg('capcha/1'),
        findImg('capcha/2'),
        findImg('capcha/3'),
        findImg('capcha/4'),
        findImg('capcha/5'),
        findImg('capcha/6'),
    ]

    sortedCoords = list(capchaCoords)

    print(sortedCoords)

    countI = len(capchaCoords) - 1

    print('Sorting...')

    # Sort coords
    while countI:
        for i in range(countI):
            x, y = sortedCoords[i]
            nextX, nextY = sortedCoords[i + 1]
            if y > nextY + 20 or not nextY > y + 20 and x > nextX:
                sortedCoords[i] = (nextX, nextY)
                sortedCoords[i + 1] = (x, y)
        countI = countI - 1

    print(capchaCoords)
    print(sortedCoords)
    countI = len(capchaCoords) - 1

    for i in range(countI):
        if capchaCoords[i] != sortedCoords[i]:
            niceMove(capchaCoords[i])
            niceDrag(sortedCoords[i])
            j = capchaCoords.index(sortedCoords[i])
            capchaCoords[i], capchaCoords[j] = capchaCoords[j], capchaCoords[i]

    print('made it')

    niceClick('btn/ready', size=3)
    print('Capcha finished')
