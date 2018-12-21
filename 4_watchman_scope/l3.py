# Fri Dec 21 15:42:20 EST 2018

import numpy as np
import matplotlib.pyplot as plt
from ROOT import TH1F

###################################################################
# Parameters for the signal
show_plot = False
N = 4002              # Signal window size
fsps = 20000000000.   # Hz, Samples per second
# NMAX = 10000000000    # Max number of files
NMAX = 200
t0 = 15.E-9           # Starting point for analysis window
t1 = 150.E-9          # Ending point for analysis window
show_plot = False

# Analysis arrays
charge = [] # Number of electrons in pulse widow
time_20p = [] # 20% crossing time
time_50p = [] # 50% crossing time
time_80p = [] # 80% crossing time
amp = []      # peak amplitude 
rise = []     # Rise time

###################################################################
# Analysis arrays
ilist = []
fin = open('./a2_data/a2_sel.txt')
for line in fin: 
    ilist.append(int(line.split()[0]))
fin.close()

n = 0
for i in ilist:
    fin = open('/media/tyler/Seagate Expansion Drive/20181220_watchman_spe_filter/l1/%05d.txt' % i)
    if(i%100==0): 
        print i
    x = []
    y = []
    for line in fin: 
        x.append(float(line.split(',')[0]))
        y.append(float(line.split(',')[1]))
    
    if show_plot:
        plt.plot(x,y)
        plt.ylim(-0.0250,0.005)
        plt.show()
        
    fin.close()

    if n == NMAX: 
        break
    
    # Find peak amplitude 
    peak_amp = np.min(y)
    amp.append(peak_amp)

    # Align the waveforms
    found_50p = False
    for ix,iy in zip(x,y): 
        if not found_50p: 
            if iy < peak_amp*0.5: 
                t_50p = ix
                break
    x1 = [xi - t_50p for xi in x]
    fname = '/media/tyler/Seagate Expansion Drive/20181220_watchman_spe_filter/l3/%05d.txt' % n
    fout = open(fname,'w')
    for x1i,yi in zip(x1,y): 
        strout = '%E,%f\n' % (x1i,yi)
        fout.write(strout)
    fout.close()
    n+=1

    # Find histogram values
    found_20p = False
    found_50p = False
    found_80p = False
    q = 0.
    for ix,iy in zip(x1,y): 
        if not found_20p: 
            if iy < peak_amp*0.2: 
                t_20p = ix
                time_20p.append(t_20p)
                found_20p = True
        if not found_50p: 
            if iy < peak_amp*0.5: 
                t_50p = ix
                time_50p.append(t_50p)
                found_50p = True
        if not found_80p: 
            if iy < peak_amp*0.8: 
                t_80p = ix
                time_80p.append(t_80p)
                found_80p = True
        q=q+(iy*1/fsps)/(50*1.6E-19) # Simple rectangular integration, small error
    charge.append(q)
    rise.append(t_80p - t_20p)
    
# Histogram values
plt.hist(charge,50)
plt.title('charge')
# plt.savefig('./a1_data/charge.png')
plt.show()
plt.hist(time_20p,50)
plt.title('time_20p')
# plt.savefig('./a1_data/time_20p.png')
plt.show()
plt.hist(time_50p,50)
plt.title('time_50p')
# plt.savefig('./a1_data/time_50p.png')
plt.show()
plt.hist(time_80p,50)
plt.title('time_80p')
# plt.savefig('./a1_data/time_80p.png')
plt.show()
plt.hist(amp,50)
plt.title('amp')
# plt.savefig('./a1_data/amp.png')
plt.show()
plt.hist(rise,50)
plt.title('rise')
# plt.savefig('./a1_data/rise.png')
plt.show()

h_20p = TH1F('h_20p','',200,-5.E-9,5.E-9)
for ti in time_20p: 
    h_20p.Fill(ti)
h_20p.Draw()
raw_input()

h_80p = TH1F('h_80p','',200,-5.E-9,5.E-9)
for ti in time_80p: 
    h_80p.Fill(ti)
h_80p.Draw()
raw_input()

