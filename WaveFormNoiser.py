#!/usr/bin/env python 

################################################
#
# Tyler Anderson
# Mon Mar 12 15:32:19 EDT 2018
#
# Generate a pulse-shaped waveform in python.
#
################################################
import numpy as np

class WaveFormNoiser:
    """A simple class to "noise" waveforms"""
    
    def __init__(self,sigma_v=1.,fsps=10.):
        self.sigma_v=sigma_v
        self.fsps=fsps

    def smear_v(self,v): 
        # print 'sigma_v = %f' % self.sigma_v
        return np.array([vi + np.random.normal(0,self.sigma_v) for vi in v])

    def smear_t(self,t): 
        tshift = np.random.uniform(0.,1./self.fsps)
        # print 'tshift = %f' % tshift
        return np.array([ti + tshift for ti in t]) 

    
