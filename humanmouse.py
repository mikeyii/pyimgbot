#!/usr/bin/env python3
from pymouse import PyMouse
import time
from math import pi, sin, pow, fabs, sqrt, ceil
import random

m = PyMouse()

class Config:
    sinWidthX = random.uniform(-35, 33)
    sinWidthY = random.uniform(-31, 32)
    sinCountX = random.randint(1, 3)
    sinCountY = random.randint(1, 4)

def easeIn(power, t):
    return pow(t, power)

def easeOut(power, t):
    return 1 - fabs(pow(t-1, power))

def easeInOut(power1, power2, t):
    if t < 0.5:
        return easeIn(power1, t*2)/2
    else:
        return easeOut(power2, t*2 - 1)/2+0.5

def getPointOnLine(x1, y1, x2, y2, n):
    windX = random.uniform(-2, 2)
    windY = random.uniform(-2, 2)

    generalNoiseK = sin(pi * n) # 0 = 0, 0.5 = 1, 1 = 1

    sinNoiseX = sin(pi * n * Config.sinCountX) # 0 0 0.5 = 1 1 = 1
    sinNoiseY = sin(pi * n * Config.sinCountY) # 0 0 0.5 = 1 1 = 1


    x = (x2 - x1) * easeInOut(2, 3, n) + sinNoiseX * Config.sinWidthX * generalNoiseK + windX * generalNoiseK + x1

    y = (y2 - y1) * easeIn(2, n) + sinNoiseY * Config.sinWidthY * generalNoiseK + windY * generalNoiseK + y1

    return (x, y)


def tween(t):
    return easeInOut((2, 4), t) #0.02


def humanMove(x = None, y = None):
    speed = random.randint(200, 400)
    startx, starty = m.position()
    dx = x - startx
    dy = y - starty


    Config.sinWidthX = random.uniform((-dx - 20) / 20, (dx + 20) / 20)
    Config.sinWidthY = random.uniform((-dy - 20) / 20, (dy + 20) / 20)

    if dy > 500:
        Config.sinCountX = random.randint(1, 4)
    else:
        Config.sinCountX = random.randint(1, 2)

    if dx > 500:
        Config.sinCountY = random.randint(1, 4)
    else:
        Config.sinCountY = random.randint(1, 2)


    distance = sqrt(dx*dx + dy*dy)
    if distance < 200:
        speed = random.randint(100, 200)
    duration = distance / speed
    print(duration)

    # 120 movements per second.
    num_steps = int(max(1.0, duration * 120.0))
    print(range(int(num_steps)))


    width, height = m.screen_size()

    # Make sure x and y are within the screen bounds.
    x = max(0, min(x, width - 1))
    y = max(0, min(y, height - 1))


    sleep_amount = duration / num_steps

    steps = [
        getPointOnLine(startx, starty, x, y, n/num_steps)
        for n in range(num_steps)
    ]
    steps.append((x, y))
    # print(steps)


    for tweenX, tweenY in steps:

        m.move(tweenX, tweenY)
        time.sleep(sleep_amount)
