import sys
sys.path.append('../')
import numpy as np
import GenPulseClass
import matplotlib.pyplot as plt

x = np.arange(0,100,0.1,dtype=float)
gpc = GenPulseClass.GenPulseClass(0,10,30,2,10,2)
y = np.array([gpc.eval(xi) + np.random.normal(0,1) for xi in x])

# print x
# print y

plt.plot(x,y)
plt.show()
