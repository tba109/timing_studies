# Fri Dec 21 16:46:58 EST 2018

import sys
sys.path.append('../')
import numpy as np
import matplotlib.pyplot as plt
import downsample

for i in range(8010):
    fin = open('/media/tyler/Seagate Expansion Drive/20181220_watchman_spe_filter/l3/%05d.txt' % i)
    print i
    x = []
    y = []
    for line in fin: 
        x.append(float(line.split(',')[0]))
        y.append(float(line.split(',')[1]))
    fin.close()

    # 1.) Downsample
    x1,y1 = downsample.downsample(x,y,dsf=40)
    
    plt.plot(x,y)
    plt.plot(x1,y1,'o')
    plt.ylim(-0.0250,0.005)
    plt.show()

    
