#!/usr/bin/env python 

################################################
#
# Tyler Anderson
# Tue Mar 13 17:36:37 EDT 2018
#
# Receive a numpy array and find the first
# sample over threshold
#
################################################
import numpy as np

class DigDiscClass:
    """A simple class to receive a numpy array and find the first point over threshold"""

    def __init__(self,vthr=0.):
        self.vthr=vthr

    def disc(self,t,v):
        for vi,ti in zip(v,t): 
            if vi > self.vthr:
                return ti
