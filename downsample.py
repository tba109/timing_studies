################################################
#
# Tyler Anderson
# Sun May 20 17:55:20 EDT 2018
#
# Downsample oscilloscope data
#
################################################
import numpy as np

def downsample(t,v,dsf=40): 
    t2 = np.array([])
    v2 = np.array([])
    icnt = 0
    istart = np.random.randint(0,dsf)
    t1 = t[istart:]
    v1 = v[istart:]
    for ti,vi in zip(t1,v1): 
        if(icnt%dsf==0): 
            t2 = np.append(t2,ti)
            v2 = np.append(v2,vi)
        icnt+=1
    return t2,v2
