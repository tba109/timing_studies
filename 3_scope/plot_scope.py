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
NCNT = 1000  # Number of triggers to collect
TAU = 8.     # First order analog filter time constant (ns)
FGSPS = 1  # Sample rate (GSPS)
VTHR = -2.0  # Discriminator threshold (mV)
NAVG1 = 2    # Box car averager 1 number of samples
CFDD = 2     # CFD delay in clock cycles 
CFDTHR = 1.0 # CFD threshold (mV)

ddc = DigDiscClass.DigDiscClass(VTHR)
lpf = LpfClass.LpfClass()

tz = np.array([])
i = 0
for fname in os.listdir(directory):
    # print fname
    t1,v1 = read_scope.read_scope(directory + fname)

    # Analog filtering and downsampling        
    v2 = lpf.lpfFirstOrder(v1,TAU,10) # 8 ns shaping, 10GSPS
    t2 = t1
    t3,v3 = downsample.downsample(t2,v2,10./FGSPS) # 250MSPS
    # print '%f' % (1./(t3[1] - t3[0]))

    # Discriminator
    found,tddc = ddc.disc_neg(t3,v3)
    if(found):
        # Boxcar
        t4,v4 = boxcar.boxcar(t3,v3,NAVG1)
        
        # Constant fraction discriminator
        t5,v5 = cfd.cfd(t4,v4,CFDD)
        
        # Zero crossing
        tzc = zero_crossing.zero_crossing(t5,v5,CFDTHR)
        tz = np.append(tz,tzc)
        
        # Plot 
        # plt.plot(t1,v1) # Full BW, 10GSPS
        # plt.plot(t2,v2) # LPF to simulate front end
        plt.plot(t3,v3,'.-',color='b') # Downsampled
        plt.plot(t4,v4,'.-',color='g') # Box car
        plt.plot(t5,v5,'.-',color='r') # CFD
        plt.axvline(tzc)
        plt.axhline(0)
        plt.xlim(t1.min(),t1.max())
        plt.ylim(-10,5)
        print i,tddc,tzc
        # plt.show()
        
        i+=1
    if(i > NCNT): 
        break
        
# tz = [tzi - 80 - 0.7055 for tzi in tz]
tz = [tzi - 70 for tzi in tz]
h1 = TH1F('h1','',400,-40,40)
for tzi in tz: 
    if(tzi < 20 and tzi > -20):
        h1.Fill(tzi)

hmean = h1.GetMean()
hrms = h1.GetRMS()

f1 = TF1('f1','gaus',-40,40)
h1.Fit('f1')
p0 = f1.GetParameter(0)
p1 = f1.GetParameter(1)
p2 = f1.GetParameter(2)

fout = open("spread.txt",'a')
sout = "directory=%s NCNT=%d TAU=%f FGSPS=%f VTHR=%f NAVG1=%f CFDD=%f CFDTHR=%f const=%f mean=%f sigma=%f HMEAN=%f HRMS=%f\n" % (directory,NCNT,TAU,FGSPS,VTHR,NAVG1,CFDD,CFDTHR,p0,p1,p2,hmean,hrms)
print sout
fout.write(sout)
fout.close()
h1.Draw()
