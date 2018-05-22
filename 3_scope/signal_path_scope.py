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
TAU = 16              # 1st order LPF time constant (ns)
NFO = 4               # Bessel filter order
FBK = 125.            # Bessel filter knee (Hz)
FGSPS = 0.25          # Sample rate (GSPS)
VTHR = -0.75          # Discriminator threshold (mV)
NAVG1 = 4             # Box car averager 1 number of samples

ddc = DigDiscClass.DigDiscClass(VTHR)
lpf = LpfClass.LpfClass()

phd = np.array([])
i = 0
for fname in os.listdir(directory):
    # print fname
    t1,v1 = read_scope.read_scope(directory + fname)

    # Shaping filter    
    v2 = lpf.lpfFirstOrder(v1,TAU,10) # shaping, 10GSPS
    t2 = t1
    
    # Simulate antialiasing filter (bessel)
    b,a = scipy.signal.bessel(NFO,FBK/(10000./2.),'low')
    # v2 = scipy.signal.filtfilt(b, a, v1)
    v2 = scipy.signal.filtfilt(b, a, v2)
    t2 = t1

    # Downsample
    t3,v3 = downsample.downsample(t2,v2,10./FGSPS) # 250MSPS
    
    # Discriminator
    found,tddc = ddc.disc_neg(t3[10:],v3[10:])
    if(found):
        plt.plot(t1,v1) # Full BW, 10GSPS
        
        # plt.plot(t2,v2,'.-') # LPF to simulate front end
        
        # Downsample
        t3,v3 = downsample.downsample(t2,v2,10./FGSPS) # 250MSPS
        plt.plot(t3,v3,'.-') # LPF to simulate front end
        
        # Boxcar
        t4,v4 = boxcar.boxcar(t3,v3,NAVG1)
        plt.plot(t4,v4,'.-')
        
        # plt.xlim(t1.min(),t1.max())
        plt.xlim(50,200)
        plt.ylim(-8,2)
        plt.show()
        
        phd = np.append(phd,v3.min())

        i+=1
    
        if(i%10==0):
            print i
    
    if(i > NCNT): 
        break

h1 = TH1F('h1','',100,-10,10)

print phd

for phdi in phd: 
    h1.Fill(phdi)

h1.Draw()
