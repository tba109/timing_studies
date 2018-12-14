import sys
sys.path.append('../')
import numpy as np
import matplotlib.pyplot as plt
import csv
import read_scope
import os
import LpfClass
import downsample
import DigDiscClass
import boxcar
import cfd
import zero_crossing
from ROOT import TH1F, TF1

# directory = '/home/tyler/pingudata/1200v/' # 10GSPS 
directory = '/home/tyler/pingudata/1300v/' # 10GSPS
NCNT = 1000           # Number of triggers to collect
TAU = [2,4,8,16,32]   # First order analog filter time constant (ns)
FGSPS = 0.5           # Sample rate (GSPS)
VTHR = -2.0           # Discriminator threshold (mV)
NAVG1 = 2             # Box car averager 1 number of samples

ddc = DigDiscClass.DigDiscClass(VTHR)
lpf = LpfClass.LpfClass()

tz = np.array([])
i = 0
for fname in os.listdir(directory):
    # print fname
    t1,v1 = read_scope.read_scope(directory + fname)

    # Analog filtering and downsampling        
    v2 = lpf.lpfFirstOrder(v1,8,10) # 8 ns shaping, 10GSPS
    t2 = t1
    t3,v3 = downsample.downsample(t2,v2,10./FGSPS) # 250MSPS
    # print '%f' % (1./(t3[1] - t3[0]))

    # Discriminator
    found,tddc = ddc.disc_neg(t3,v3)
    if(found):
        for taui in TAU: 
            # Plot 
            # plt.plot(t1,v1) # Full BW, 10GSPS
            
            v2 = lpf.lpfFirstOrder(v1,taui,10) # 8 ns shaping, 10GSPS
            t2 = t1
            # plt.plot(t2,v2,'.-') # LPF to simulate front end

            t3,v3 = downsample.downsample(t2,v2,10./FGSPS) # 250MSPS
            plt.plot(t3,v3,'.-') # LPF to simulate front end
            
            # plt.xlim(t1.min(),t1.max())
            plt.xlim(50,200)
            plt.ylim(-8,2)
        plt.show()
        i+=1
    if(i > NCNT): 
        break
