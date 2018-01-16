#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
x = 100
y = 100

tck,u = interpolate.splprep([x,y],s=3)
unew = np.arange(0,1.01,0.01)
out = interpolate.splev(unew,tck)
plt.figure()
plt.plot(x,y,out[0],out[1])
plt.show()
