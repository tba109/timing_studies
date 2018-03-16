#!/usr/bin/env python 

################################################
#
# Tyler Anderson
# Fri Mar 16 16:30:47 EDT 2018
#
# Low Pass Filter 
#
################################################
import numpy as np

class LpfClass:
    """Low pass filter waveforms"""
        
    def lpfFirstOrder(self,x,tau=2.,fsps=10.):
        alpha = 1-np.exp(-1./(fsps*tau))
        y = np.zeros(len(x))
        print alpha
        for i in range(len(x)): 
            if(i == 0): 
                y[i] = x[i]
            else:
                y[i] = x[i]*alpha + (1-alpha)*y[i-1]
        return y
