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
import scipy.signal

# directory = '/home/tyler/pingudata/1200v/' # 10GSPS 
directory = '/home/tyler/pingudata/1300v/' # 10GSPS
NCNT = 1000           # Number of triggers to collect
TAU = 8               # 1st order LPF time constant (ns)
NFO = [2,4,6,8]       # Bessel filter order
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
    v2 = lpf.lpfFirstOrder(v1,TAU,10) # shaping, 10GSPS
    t2 = t1
    
    # Downsample
    t3,v3 = downsample.downsample(t2,v2,10./FGSPS) # 250MSPS
    
    # Discriminator
    found,tddc = ddc.disc_neg(t3,v3)
    if(found):
        # plt.plot(t1,v1) # Full BW, 10GSPS
        for nfoi in NFO: 
            # Plot 
            
            # Simulate bessel filter
            b,a = scipy.signal.bessel(nfoi,125./(10000./2.),'low')
            # v2 = scipy.signal.filtfilt(b, a, v1)
            v2 = scipy.signal.filtfilt(b, a, v1)
            t2 = t1
            # plt.plot(t2,v2,'.-') # LPF to simulate front end

            # Downsample
            t3,v3 = downsample.downsample(t2,v2,10./FGSPS) # 250MSPS
            plt.plot(t3,v3,'.-') # LPF to simulate front end
            
            # plt.xlim(t1.min(),t1.max())
            plt.xlim(50,200)
            plt.ylim(-8,2)
        plt.show()
        i+=1
    if(i > NCNT): 
        break

