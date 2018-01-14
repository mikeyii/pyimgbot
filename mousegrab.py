#!/usr/bin/env python3

from pymouse import PyMouseEvent
import items
from time import sleep

class MouseHandler(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)

    def click(self, x, y, button, press):
        '''Handle clicks.'''
        print(x, y, button, press)
        x = int(x)
        y = int(y)
        fileStr = "mouse {} {} \n".format(x, y)
        print(fileStr, end='')
        sleep(5)
        result = items.getItems(160, ('Агат', 'Аквамарин', 'Бирюза'))
        if len(result) == 1:
            i = result[0]
            fileStr += "{} {} {}\n".format((i['name']), i['x'], i['y'])
            fileStr += "difference {} {}\n".format(x - i['x'], y - i['y'])
            print(fileStr, end='')
            with open('mouse.txt', 'w') as logFile:
                logFile.write(fileStr)
            print('String captured')
        else:
            print("Items len is ", len(result))
        print('waiting for next click')


    def close(self):
        print('Close file')
        self.logFile.close()




try:
    sleep(5)
    C = MouseHandler()
    C.run()
except KeyboardInterrupt:
    print('\nBye')
