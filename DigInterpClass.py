#!/usr/bin/env python 

################################################
#
# Tyler Anderson
# Fri Mar 16 07:42:06 EDT 2018
#
# Receive a numpy array and interpolate down to
# t=0 axis
#
################################################
import numpy as np
from scipy.optimize import curve_fit
class DigInterpClass:
    """A simple class to receive a numpy array and interpolate the rising edge at a threshold"""

    def __init__(self,vthr=0.,n=5.):
        self.vthr=vthr
        self.n=n

    def disc_interp(self,t,v):
        # Fit the curves
        def f(x,m,b): 
            return m*x + b        

        for i in range(len(t)): 
            if v[i] > self.vthr:
                # print t
                # print v
                # print self.n
                # print i
                ilow = i-self.n
                ihigh = i+self.n
                # print ilow
                # print ihigh
                # print t[ilow:ihigh]
                # print v[ilow:ihigh]
                # print self.n
                # print i
                popt,pcov = curve_fit(f,t[ilow:ihigh],v[ilow:ihigh])
                # return -popt[1]/popt[0]
                return popt
                
    
