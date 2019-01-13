import sys
import numpy as np
import matplotlib.pyplot as plt

###############################################################################################
# Constant fraction discriminator
def cfd(t,x,d=1):     
    # Differentiate
    x2 = [xi - xj for xi,xj in zip(x[:-1*d],x[d:])]
    t2 = t[d:]    
    return t2,x2

###############################################################################################
# CFD sort of like what CAEN does
# y = x[i]*f - x[i-d]
# n: number of samples in moving average
# d: delay
# f: fractional attenuation
# Note: the filtering shifts the zero crossing some what...need to think about how to deal with this
def cfdb(t,x,n=1,d=1,f=0.5,show_plot=False):
    if n <= 0: 
        print 'error! require n >= 1'
        sys.exit()
    # if show_plot is True:
        # plt.axvline(11.5)
        # plt.axhline(thr)
        # plt.axhline(0.)
        # plt.plot(t,x)
    # Windowed averaging
    x2 = np.zeros(len(x)-n+1)
    t2 = np.zeros(len(t)-n+1)
    for i in range(len(x)-n+1): 
        t2[i] = t[i+n-1]
        xsum = 0.
        for ii in range(n): 
            xsum = xsum+x[i+ii]
        x2[i] = float(xsum)/float(n)
    if show_plot is True:
        plt.plot(t2,x2,color='blue')
    # Attenuation
    t3 = [t2i for t2i in t2[:-d]]
    x3 = [x2i*f for x2i in x2[d:]]
    if show_plot is True:
        plt.plot(t3,x3,color='red')
    # Difference 
    t4 = [t3i for t3i in t3]
    x4 = [x3i-x2i for x3i,x2i in zip(x3,x2)]
    if show_plot is True:
        plt.plot(t4,x4,color='green')
        plt.show()
    return t4,x4

###############################################################################################
# CFD sort of like what CAEN does
# y = x[i]*f - x[i-d]
# n1: number of samples in first moving average
# d: delay
# n2: number of samples in second moving average
# f: fractional attenuation
# Note: the filtering shifts the zero crossing some what...need to think about how to deal with this
def cfdc(t,x,n1=1,d=1,n2=1,f=0.5,show_plot=False):
    if n1 <= 0: 
        print 'error! require n >= 1'
        sys.exit()
    # if show_plot is True:
        # plt.axvline(11.5)
        # plt.axhline(thr)
        # plt.axhline(0.)
        # plt.plot(t,x)
    # Windowed averaging
    x2 = np.zeros(len(x)-n1+1)
    t2 = np.zeros(len(t)-n1+1)
    for i in range(len(x)-n1+1): 
        t2[i] = t[i+n1-1]
        xsum = 0.
        for ii in range(n1): 
            xsum = xsum+x[i+ii]
        x2[i] = float(xsum)/float(n1)
    if show_plot is True:
        plt.plot(t2,x2,color='blue')
    # Attenuation
    t3 = [t2i for t2i in t2[:-d]]
    x3 = [x2i*f for x2i in x2[d:]]
    if show_plot is True:
        plt.plot(t3,x3,color='red')
    # Difference 
    t4 = [t3i for t3i in t3]
    x4 = [x3i-x2i for x3i,x2i in zip(x3,x2)]
    if show_plot is True:
        plt.plot(t4,x4,color='green')
        plt.show()
    # Average once more
    x5 = np.zeros(len(x4)-n2+1)
    t5 = np.zeros(len(t4)-n2+1)
    for i in range(len(x4)-n2+1): 
        t5[i] = t4[i+n2-1]
        xsum = 0.
        for ii in range(n2): 
            xsum = xsum+x4[i+ii]
        x5[i] = float(xsum)/float(n2)
    return t5,x5


#############################################################################################
# Test functions
def main():
    show_plot = True
    # show_plot = False
    t1 = np.arange(100)
    x1 = np.zeros(100)
    for i in range(10,20): 
        x1[i] = 1.
    t2,x2 = cfdb(t1,x1,n=5,d=5,f=0.5,show_plot=show_plot)

if __name__ == '__main__':
    main()
