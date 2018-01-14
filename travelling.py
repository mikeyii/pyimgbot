#!/usr/bin/env python3

from helper import *
import clipboard

def getCompassCoords():
    coords = findImg('compass')
    if coords:
        x, y = coords
        y = y - 20
        return x, y
    return coords


def setNavigator(location):
    print('Сначала зададим локацию в навигаторе')
    print(getCompassCoords())
    niceClick(getCompassCoords())
    waitClick('field')
    clipboard.copy(location)
    pyautogui.hotkey('command', 'v')
    if not imgExists('btn/accept'):
        print('Данной локации не существует!')
        print('Выход')
        return
    niceClick('btn/accept')
    print('🔔  Локация задана', location)
    niceClick('chat_line')

def travel(location = None):
    try:
        if location:
            setNavigator(location)
            print('А теперь пристегнитесь, начинаем путешествие в', location);
        print('Поехали')
        while imgExists('location_compass'):
            niceMove('location_compass')
            print('⏳  Ждём перехода...')
            sleepWhileImg(('cannot_go', 'cannot_go2'))
            while not imgExists('labels/map'):
                print('Something is wrong, we are not on location')
                if imgExists('vs'):
                    print('We are in the battle')
                    battle()
            print('🚗  Перемещение в новую локацию')
            niceClick('location_compass', 2)

        print('Итерация закончена')
        if imgExists('labels/map') and not imgExists('location_compass'):
            print('🎉  Путешествие окончено, поздравляем')
            return true
        else:
            travel()

    except KeyboardInterrupt:
        print('\nДо новых встреч!')

def battle():
    waitClick('btn/exit')
    waitClick('btn/in_location')
    waitClick('btn/capital')

def main():
    location = input('Введите новую локацию: ')

    niceClick('chat_line') # focus window

    if not imgExists('labels/map'):
        niceClick('location')

    travel(location)

if __name__ == '__main__':
    main()
