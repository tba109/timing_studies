# Fri Dec 21 10:46:16 EST 2018

import numpy as np
import matplotlib.pyplot as plt
from ROOT import TH1F

###################################################################
# Parameters for the signal
show_plot = False
N = 4002              # Signal window size
fsps = 20000000000.   # Hz, Samples per second
NFILES = 16922        # Number of reduced files
# NFILES = 200
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
n0 = int(t0*fsps)
n1 = int(t1*fsps)
for i in range(1,NFILES+1):
    fin = open('/media/tyler/Seagate Expansion Drive/20181220_watchman_spe_filter/l1/%05d.txt' % i)
    # Header
    if(i%100==0): 
        print i
    for j in range(5): 
        fin.readline()
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
        
    # 1.) Select the analysis window 
    x1 = x[n0:n1]
    y1 = y[n0:n1]
    
    # 2.) Find peak amplitude 
    peak_amp = np.min(y1)
    amp.append(peak_amp)

    # 3.) Find histogram values
    found_20p = False
    found_50p = False
    found_80p = False
    q = 0.
    for ix,iy in zip(x1,y1): 
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
    
# 4.) Write data words out
fout = open('./a1_data/a1_data.txt','w')
i = 1
for chargei,t_20pi,t_50pi,t_80pi,ampi,risei in zip(charge,time_20p,time_50p,time_80p,amp,rise):
    strout = '%d %E %E %E %E %E %E\n' % (i,chargei,t_20pi,t_50pi,t_80pi,ampi,risei)
    fout.write(strout)
    i+=1
fout.close()

# 5.) Histogram values
plt.hist(charge,50)
plt.title('charge')
plt.savefig('./a1_data/charge.png')
plt.show()
plt.hist(time_20p,50)
plt.title('time_20p')
plt.savefig('./a1_data/time_20p.png')
plt.show()
plt.hist(time_50p,50)
plt.title('time_50p')
plt.savefig('./a1_data/time_50p.png')
plt.show()
plt.hist(time_80p,50)
plt.title('time_80p')
plt.savefig('./a1_data/time_80p.png')
plt.show()
plt.hist(amp,50)
plt.title('amp')
plt.savefig('./a1_data/amp.png')
plt.show()
plt.hist(rise,50)
plt.title('rise')
plt.savefig('./a1_data/rise.png')
plt.show()

# 6.) Explore cuts to find SPEs
q_cut_0     = -1.6E6
q_cut_1     = -2.5E7
t_50p_cut_0 = 0.3E-7
t_50p_cut_1 = 0.6E-7
amp_cut_0   = -0.0005
t_rise_0    = 2.E-9
fin = open('./a1_data/a1_data.txt')
fout = open('./a1_data/a1_sel.txt','w')
for line in fin: 
    i = int(line.split()[0])
    q = float(line.split()[1])
    t_20p = float(line.split()[2])
    t_50p = float(line.split()[3])
    t_80p = float(line.split()[4])
    a = float(line.split()[5])
    r = float(line.split()[6])
    if (
        q < q_cut_0 and
        q > q_cut_1 and 
        t_50p > t_50p_cut_0 and
        t_50p < t_50p_cut_1 and 
        a < amp_cut_0): 
        fout.write(line)
        print line[:-1],'   ',i,q,t_20p,t_50p,t_80p,a,r
fin.close()
fout.close()

