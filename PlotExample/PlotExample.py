import numpy as np
import pylab
import matplotlib.pyplot as plt
t = np.arange(0.0, 1.0+0.1, 0.01)
s = np.cos(2*2*np.pi*t)

pylab.plot(t,s)
pylab.grid(True)
pylab.xticks([i/100.0 for i in range(0,120)])
pylab.show()

