import sys
sys.path.append('../')
import numpy as np
import GenPulseClass
import matplotlib.pyplot as plt
import DigInterpClass
import DigDiscClass
import WaveFormNoiser
from scipy.optimize import curve_fit
import LpfClass

# This is really simple: I just want to see how time constant effects overall RMS noise

# Waveform parameters
# fsps = np.array([1.])
# fsps = np.arange(1.,11.,1.)
# fsps = [10.]
fsps = [10.]
Nwaves = 10000
v0 = 0.
# v1 = np.arange(10.,110.,10.)
v1 = np.array([10.])
tdelay = 5.
# trise = np.arange(1.,11.,1.)
trise = np.array([10])
ton = 10.
tfall = 10
# sigma_v = np.arange(0.1,1,0.1)
sigma_v = np.array([1])
vthr = 5.

tau = np.arange(0,10.,.1)

# Sigma
sigma_y = np.zeros(len(tau))
sigma_y2 = np.zeros(len(tau))

for i in range(len(tau)): 
    wfn = WaveFormNoiser.WaveFormNoiser(sigma_v[0],fsps[0])
    x = np.arange(0,1000,1./fsps[0],dtype=float)
    x = wfn.smear_t(x)
    gpc = GenPulseClass.GenPulseClass(v0,v1[0],tdelay,trise[0],ton,tfall)
    # y = np.array([gpc.eval(xi) for xi in x])
    y = np.zeros(len(x))
    y = wfn.smear_v(y)
    lpf = LpfClass.LpfClass()
    y2 = lpf.lpfFirstOrder(y,tau[i],fsps[0])
    
    # plt.plot(x,y,'o-',color='b')
    # plt.plot(x,y2,'o-',color='r')
    # plt.show()

    sigma_y[i] = np.std(y)
    sigma_y2[i] = np.std(y2)

print sigma_y2

plt.plot(tau,sigma_y,'o-',color='blue')
plt.plot(tau,sigma_y2,'o-',color='red')
plt.show()

plt.semilogx(tau,[100*sy2/sy for (sy,sy2) in zip(sigma_y,sigma_y2)],'o-')
# plt.plot(tau,[100*sy2/sy for (sy,sy2) in zip(sigma_y,sigma_y2)],'o-')
plt.show()

# Looks like the answer is an LPF creates a fixed percent noise reduction with amplitude
