import sys
import numpy as np
import matplotlib.pyplot as plt

###############################################################################################
# Trapazoidal integrator
def trap_int(t,x,n0,n1):     
    xsum = 0.
    dt = t[1]-t[0]
    for i in range(n0,n1,1):
        xsum+=dt*(x[i] + (x[i+1]-x[i])*0.5)
    return xsum
#############################################################################################
# Test functions
def main():
    print 'hi'

if __name__ == '__main__':
    main()
