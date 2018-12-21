# Fri Dec 21 16:46:58 EST 2018

import sys
sys.path.append('../')
import numpy as np
import matplotlib.pyplot as plt
import downsample
import LpfClass
from ROOT import TH1F

###################################################################
# Parameters for study
NFILES = 8010
# NFILES = 200
TAU = 16.E-9               # 1st order LPF time constant 
SCOPE_FSPS = 20000000000.  # Oscilloscope sample rate
DIG_FSPS   = 500000000.    # Digitizer sample rate
VTHR = -0.005              # Discriminator threshold (mV)
show_waveform = False

lpf = LpfClass.LpfClass()
peak = []
time_50p = []
time_50p_interp = []
for i in range(NFILES):
    fin = open('/media/tyler/Seagate Expansion Drive/20181220_watchman_spe_filter/l3/%05d.txt' % i)
    if(i%100==0):
        print i
    x = []
    y = []
    for line in fin: 
        x.append(float(line.split(',')[0]))
        y.append(float(line.split(',')[1]))
    fin.close()

    # 1.) Low pass filter
    y1 = lpf.lpfFirstOrder(y,TAU,SCOPE_FSPS)

    # 2.) Downsample
    x2,y2 = downsample.downsample(x,y1,dsf=SCOPE_FSPS/DIG_FSPS)
    
    # print len(x),len(y),len(y1),len(y2)
    
    if show_waveform: 
        plt.plot(x,y)
        plt.plot(x,y1)
        plt.plot(x2,y2,'o')
        plt.ylim(-0.0250,0.005)
        plt.show()

    # 3.) CFD with no interpolation

    pk = np.min(y2)
    peak.append(pk)
    xprev = 0.
    yprev = 0.
    for x2i,y2i in zip(x2,y2): 
        if y2i < 0.5*pk: 
            time_50p.append(x2i)
            tinterp = xprev + ((x2i-xprev)/(y2i-yprev))*0.5*pk
            time_50p_interp.append(tinterp)
            xprev = x2i
            yprev = y2i
            break

# Summary data
plt.hist(peak)
plt.title('peak')
plt.show()

plt.hist(time_50p)
plt.title('time_50p')
plt.show()

h0 = TH1F('h0','',100,-0.010,0)
for pi in peak: 
    h0.Fill(pi)
h0.Draw()
raw_input()

h1 = TH1F('h1','',100,0.E-9,10.E-9)
for ti in time_50p: 
    h1.Fill(ti)
h1.Draw()
raw_input()

h2 = TH1F('h2','',100,0.E-9,10.E-9)
for ti in time_50p_interp: 
    h2.Fill(ti)
h2.Draw()
raw_input()
