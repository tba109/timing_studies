import sys
sys.path.append('../')
import numpy as np
import GenPulseClass
import matplotlib.pyplot as plt
import DigDiscClass

# Waveform parameters
fsps = 10.
Nwaves = 1000
v0 = 0.
v1 = 10.
tdelay = 30.
trise = 2.
ton = 10.
tfall = 2.
sigma_v = 1.
vthr = 5.

x = np.arange(0,100,1./fsps,dtype=float)
gpc = GenPulseClass.GenPulseClass(v0,v1,tdelay,trise,ton,tfall)
ddc = DigDiscClass.DigDiscClass(vthr)
tdisc = np.zeros(Nwaves)

for i in range(Nwaves): 
    y = np.array([gpc.eval(xi) + np.random.normal(0,sigma_v) for xi in x])
    # print x
    # print y
    plt.plot(x,y)
    plt.show()
    tdisc[i] = ddc.disc(x,y)

print len(tdisc)
plt.hist(tdisc,1000,(0,100))
plt.yscale('log')
print np.std(tdisc)
plt.show()

