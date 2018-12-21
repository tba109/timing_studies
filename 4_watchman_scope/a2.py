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
show_plot = False     # Show the plot
show_record = True    # Show the record

# Analysis arrays
charge = []   # Number of electrons in pulse widow
time_20p = [] # 20% crossing time
time_50p = [] # 50% crossing time
time_80p = [] # 80% crossing time
amp = []      # peak amplitude 
rise = []     # Rise time

# For cuts (this excludes extra PE pulses)
t_late_cut = 75.E-9
v_late_cut = -0.002

###################################################################
# Analysis arrays
n0 = int(t0*fsps)
n1 = int(t1*fsps)
flist = open('a1_data/a1_sel.txt')
ilist = []
a1list = []
for line in flist: 
    ilist.append(int(line.split(' ')[0]))
    a1list.append(line)
fout = open('a2_data/a2_sel.txt','w')
for i,a1i in zip(ilist,a1list):
    fin = open('/media/tyler/Seagate Expansion Drive/20181220_watchman_spe_filter/l1/%05d.txt' % i)
    # Header
    x = []
    y = []
    for line in fin: 
        x.append(float(line.split(',')[0]))
        y.append(float(line.split(',')[1]))
    if show_plot:
        plt.plot(x,y)
        plt.ylim(-0.0250,0.005)
        plt.show()
    record = True
    for ix,iy in zip(x,y): 
        if ix > t_late_cut and iy < v_late_cut: 
            record = False
            break
    if record: 
        fout.write(a1i)
    fin.close()
    if show_record:
        if(record): 
            plt.plot(x,y,color='blue')
            pause_val = 0.0001
        else: 
            plt.plot(x,y,color='red')
            pause_val = 1.
        plt.ylim(-0.0250,0.005)
        plt.title(i)
        plt.draw()
        plt.pause(pause_val)
        plt.clf()

fout.close()

