from random import randint
from helper import findImg

class HuntMap:

    def __init__(self):
        self.isError = False

        backCoords = findImg('back')
        if not backCoords:
            print('Back button is not found')
            self.isError = True
            return

        backX, backY = backCoords
        # Type map coords
        left = backX - 420
        right = backX - 370
        top = backY - 7
        bottom = backY + 30
        middle = (top + bottom) / 2

        self.coords = (
            (left, top),
            (middle, left),
            (left, bottom),
            (top, right),
            (right, middle),
            (bottom, right)
        )
        self.coordsLen = len(self.coords)

        self.lastI = 0

    def getRandomCoords(self):
        i = randint(0, self.coordsLen - 1)
        while i == self.lastI:
            i = randint(0, self.coordsLen - 1)
        self.lastI = i
        return self.coords[i]
