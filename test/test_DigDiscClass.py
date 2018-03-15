import sys
sys.path.append('../')
import numpy as np
import GenPulseClass
import matplotlib.pyplot as plt
import DigDiscClass
from scipy.optimize import curve_fit

# Waveform parameters
fsps = 10.
Nwaves = 1000
v0 = 0.
v1 = 10.
tdelay = 30.
trise = 10.
ton = 10.
tfall = 10.
sigma_v = np.arange(0.1,1,0.1)
vthr = 5.

x = np.arange(0,100,1./fsps,dtype=float)
gpc = GenPulseClass.GenPulseClass(v0,v1,tdelay,trise,ton,tfall)
ddc = DigDiscClass.DigDiscClass(vthr)
tdisc = np.zeros(Nwaves)

sigma_t = np.zeros(len(sigma_v))

for j in range(len(sigma_v)):
    # Generate the waveforms
    for i in range(Nwaves): 
        y = np.array([gpc.eval(xi) + np.random.normal(0,sigma_v[j]) for xi in x])
        tdisc[i] = ddc.disc(x,y)
        # print tdisc[i]
        # y = np.array([gpc.eval(xi)  for xi in x])
        # print x
        # print y
        # plt.plot(x,y)
        # plt.show()

    mu = np.mean(tdisc)
    sigma = np.std(tdisc)
    sigma_t[j] = sigma
    print 'sigma = %f' % np.std(tdisc)
    # n, bins, patches = plt.hist(tdisc,1000,(0,100),normed=1)
    # plt.xlim(mu-4*sigma,mu+4*sigma)
    # plt.yscale('log')
    # plt.show()

# Fit the curves
def f(x,m,b): 
    return m*x + b

popt,pcov = curve_fit(f,sigma_v[3:-1],sigma_t[3:-1])
print popt
plt.plot(sigma_v,sigma_t,'o-')
plt.plot(sigma_v,f(sigma_v,popt[0],popt[1]),'r-')
plt.show()
