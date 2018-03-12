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

class GenPulseClass:
    """A simple class for generating pulses"""

    def __init__(self,v0=0,v1=1,tdelay=1.,trise=1.,ton=1.,tfall=1.):
        self.v0 = v0         # initial amplitude
        self.v1 = v1         # final amplitude
        self.tdelay = tdelay # pulse delay
        self.trise = trise   # pulse rise time
        self.ton = ton       # pulse on time
        self.tfall  = tfall  # pulse fall time

    def eval(self,x):
        if x <= self.tdelay:
            return self.v0
        elif x > self.tdelay and x <= (self.tdelay + self.trise):
            return self.v0 + (x-self.tdelay)*(self.v1 - self.v0)/(self.trise)
        elif x > (self.tdelay + self.trise) and x <= (self.tdelay + self.trise + self.ton):
            return self.v1
        elif x > (self.tdelay + self.trise + self.ton) and x <= (self.tdelay + self.trise + self.ton + self.tfall):
            return self.v1 + (x-(self.tdelay+self.trise+self.ton))*(self.v0 - self.v1)/(self.trise)
        else:
            return self.v0

                
    
        
