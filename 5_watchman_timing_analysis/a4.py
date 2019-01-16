# Fri Dec 21 16:46:58 EST 2018

import sys
sys.path.append('../')
import numpy as np
import matplotlib.pyplot as plt
import downsample
import LpfClass
from ROOT import TH1F
import cfd
import zero_crossing
import trap_int
import copy

###################################################################
# Parameters for study
NFILES = 8010
# NFILES = 200
TAU = 16.E-9               # 1st order LPF time constant 
SCOPE_FSPS = 20000000000.  # Oscilloscope sample rate
DIG_FSPS   = 500000000.    # Digitizer sample rate
VTHR = -0.005              # Discriminator threshold (mV)
show_waveform = False
# show_waveform = True

lpf = LpfClass.LpfClass()
peak_0 = []
time_cfd = []
time_cfd_interp = []
charge_0 = []
charge_2 = []
yavg = []
xavg = []
ymin = 0.

for i in range(NFILES):
    # fin = open('/media/tyler/Seagate Expansion Drive/20181220_watchman_spe_filter/l3/%05d.txt' % i)
    fin = open('/home/tyler/20181220_watchman_spe_filter/l3b/%05d.txt' % i)
    if(i%100==0):
        print i
    x = []
    y = []
    for line in fin: 
        x.append(float(line.split(',')[0]))
        y.append(float(line.split(',')[1]))
    fin.close()
    
    peak_0.append(np.min(y))
    # print 'np.min(y) = % d' % np.min(y)
    q = trap_int.trap_int(x,y,0,len(x)-1)
    charge_0.append(q)
    
    x3,y3 = cfd.cfdc(x,y,8,6,4,0.75,False)
    zc = zero_crossing.zero_crossing_pos(x3,y3,thr=-10.)
    time_cfd_interp.append(zc)
    # sys.exit()

    # 4.) Charge 
    if show_waveform:
        print zc
        plt.plot(x,y,marker='o',color='blue')
        plt.plot(x3,y3,marker='o',color='green')
        plt.axvline(zc)
        plt.show()    

# Summary data
plt.hist(peak_0)
plt.title('peak_0')
plt.show()

plt.hist(charge_0)
plt.title('charge_0')
plt.show()

plt.hist(time_cfd_interp)
plt.title('time_cfd_interp')
plt.show()

h1 = TH1F('h1','',100,15,35)
for tci in time_cfd_interp: 
    h1.Fill(tci)
h1.Draw()
raw_input()
