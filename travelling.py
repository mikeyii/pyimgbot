#!/usr/bin/env python3

from helper import *
import clipboard

def getCompassCoords():
    coords = findImg('labels/compass')
    if coords:
        x, y = coords
        y = y - 20
        return x, y
    return coords


def setNavigator(location):
    print('Сначала зададим локацию в навигаторе')
    niceClick(getCompassCoords(), size=5)
    waitClick('field', area=(-20, -5, 20, 5))
    clipboard.copy(location)
    pyautogui.hotkey('command', 'v')
    if not imgExists('btn/accept'):
        print('Данной локации не существует!')
        print('Выход')
        return
    niceClick('btn/accept', size=3)
    print('🔔  Локация задана', location)
    niceClick('chat_line', area=(-100, -40, 100, 40))

def travel(location = None):
    try:
        niceClick('chat_line', area=(-100, -40, 100, 40)) # focus window

        if not imgExists('labels/map'):
            print('no map label')
            niceClick('location', size=7)
            print('Please toggle map')
            sleepUntilImg('labels/map')
        print('travel')
        if location:
            setNavigator(location)
        print('Поехали')
        while imgExists('location_compass'):
            print('⏳  Ждём перехода...')
            sleepWhileImages(('cannot_go', 'cannot_go2'))
            print('Подождали')
            while not imgExists('labels/map'):
                print('Something is wrong, we are not on location')
                if imgExists('vs'):
                    print('We are in the battle')
                    battle()
            if not imgExists('location_compass'):
                print('Компаса нет')
            print('🚗  Перемещение в новую локацию')
            niceClick('location_compass', 2, area=(40, -3, 80, 3))

        print('Итерация закончена')
        if imgExists('labels/map') and not imgExists('location_compass'):
            print('🎉  Путешествие окончено, поздравляем')
            return True
        else:
            travel()

    except KeyboardInterrupt:
        print('\nДо новых встреч!')

def battle():
    waitClick('btn/exit', size=3)
    waitClick('btn/in_location', size=3)
    waitClick('btn/capital', size=3)

def main():
    location = input('Введите новую локацию: ')
    travel(location)

if __name__ == '__main__':
    main()
