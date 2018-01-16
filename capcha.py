#!/usr/bin/env python3
from helper import *

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
