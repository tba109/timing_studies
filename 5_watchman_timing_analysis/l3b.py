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
peak_1 = []
peak_2 = []
time_cfd = []
time_cfd_interp = []
charge_0 = []
charge_2 = []
yavg = []
xavg = []
ymin = 0.

# DIG parameters
DIG_RANGE_V = 0.5
DIG_B = 14
# DIG_NOISE_LSB = 2.5
DIG_NOISE_LSB = 0.001
# DIG_BASELINE = int(2**14*0.9)
DIG_BASELINE = 0
for i in range(NFILES):
    # fin = open('/media/tyler/Seagate Expansion Drive/20181220_watchman_spe_filter/l3/%05d.txt' % i)
    fin = open('/home/tyler/20181220_watchman_spe_filter/l3/%05d.txt' % i)
    if(i%100==0):
        print i
    x = []
    y = []
    for line in fin: 
        x.append(float(line.split(',')[0]))
        y.append(float(line.split(',')[1]))
    fin.close()

    # if i > 3700: 
    #     show_waveform = True

    # if len(y) != 4002: 
    #     continue
    
    fout = open('/home/tyler/20181220_watchman_spe_filter/l3b/%05d.txt' % i,'w')

    # 1.) Low pass filter
    y1 = lpf.lpfFirstOrder(y,TAU,SCOPE_FSPS)
    peak_1.append(np.min(y1))
 
    # 2.) Downsample
    x2,y2 = downsample.downsample(x,y1,dsf=SCOPE_FSPS/DIG_FSPS)
    pk = np.min(y2)
    peak_2.append(pk)
    q = trap_int.trap_int(x2,y2,0,len(x2)-1)
    charge_2.append(q/(50.*1.6*10**-19))

    # 3.) Sample with a 14b ADC, 0.5V range
    j = 0
    y3 = []
    for y2i in y2: 
        y3i = int(y2i*(2**DIG_B-1)/0.5 + np.random.normal(0,DIG_NOISE_LSB) + DIG_BASELINE)
        y3.append(y3i)
        fout.write('%d,%d\n' % (j,y3i))
        j+=1

    if show_waveform: 
        # print y3
        plt.plot(y3,'o-')
        plt.ylim(14600,14800)
        plt.show()

    fout.close()
