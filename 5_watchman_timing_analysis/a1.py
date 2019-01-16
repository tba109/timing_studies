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

    if len(y) != 4002: 
        continue

    peak_0.append(np.min(y))
    q = trap_int.trap_int(x,y,0,len(x)-1)
    charge_0.append(q/(50.*1.6*10**-19))

    ymin = np.min(y)
    yscale = [yi/ymin for yi in y]
    if(i == 0): 
        yavg = np.zeros(len(y))
        xavg = copy.copy(x)
    yavg = [(yavgi*i + yscalei)/(i+1) for yavgi,yscalei in zip(yavg,yscale)]
    # print len(xavg),len(yavg)

    # 1.) Low pass filter
    y1 = lpf.lpfFirstOrder(y,TAU,SCOPE_FSPS)
    peak_1.append(np.min(y1))
 
    # 2.) Downsample
    x2,y2 = downsample.downsample(x,y1,dsf=SCOPE_FSPS/DIG_FSPS)
    pk = np.min(y2)
    peak_2.append(pk)
    q = trap_int.trap_int(x2,y2,0,len(x2)-1)
    charge_2.append(q/(50.*1.6*10**-19))


    # 3.) CFD with no interpolation
    xprev = 0.
    yprev = 0.
    for x2i,y2i in zip(x2,y2): 
        if y2i < 0.5*pk: 
            time_cfd.append(x2i)
            # tinterp = xprev + ((x2i-xprev)/(y2i-yprev))*0.5*pk
            # time_cfd_interp.append(tinterp)
            xprev = x2i
            yprev = y2i
            break
    
    x3,y3 = cfd.cfdc(x2,y2,2,4,2,0.25,False)
    zc = zero_crossing.zero_crossing_pos(x3,y3,thr=-0.0001)
    time_cfd_interp.append(zc)
    # sys.exit()

    # 4.) Charge 
    if show_waveform:
        print zc
        plt.plot(x,y)
        plt.plot(x,y1)
        plt.plot(x2,y2,'o')
        plt.plot(x3,y3,marker='o',color='green')
        plt.axvline(zc)
        plt.axhline(0)
        # plt.axhline(-0.0005)
        plt.ylim(-0.0250,0.005)
        plt.show()
    

# Summary data
print len(xavg),len(yavg)
ymax = np.max(yavg)
yavg = [yi/(-1.*ymax) for yi in yavg]
plt.plot(xavg,yavg)
plt.show()

plt.hist(peak_0)
plt.title('peak_0')
plt.show()

plt.hist(peak_1)
plt.title('peak_1')
plt.show()

plt.hist(peak_2)
plt.title('peak_2')
plt.show()

plt.hist(time_cfd)
plt.title('time_cfd')
plt.show()

plt.hist(time_cfd_interp)
plt.title('time_cfd_interp')
plt.show()

plt.hist(charge_0)
plt.title('charge_0')
plt.show()

print 'sigma_charge_0 = %f,%f,%f' % (np.mean(charge_0),np.std(charge_0),np.std(charge_0)/np.mean(charge_0)*100.) 

plt.hist(charge_2)
plt.title('charge_2')
plt.show()

print 'sigma_charge_2 = %f,%f,%f' % (np.mean(charge_2),np.std(charge_2),np.std(charge_2)/np.mean(charge_2)*100.) 

h0 = TH1F('h0','',100,-0.010,0)
for pi in peak_2: 
    h0.Fill(pi)
h0.Draw()
raw_input()

h1 = TH1F('h1','',100,0.E-9,10.E-9)
for ti in time_cfd: 
    h1.Fill(ti)
h1.Draw()
raw_input()

h2 = TH1F('h2','',100,0.E-9,10.E-9)
for ti in time_cfd_interp: 
    h2.Fill(ti)
h2.Draw()
raw_input()

h3 = TH1F('h3','',100,-4.E7,0.)
for ti in charge_0: 
    h3.Fill(ti)
h3.Draw()
raw_input()

h4 = TH1F('h4','',100,-4.E7,0.)
for ti in charge_2: 
    h4.Fill(ti)
h4.Draw()
raw_input()

# Write the data out to file: 
fout = open('a1_out.txt','w')
for ix,iy in zip(xavg,yavg):
    lo = '%.12f,%f\n' % (ix,iy)
    fout.write(lo)
fout.close()

