import sys
sys.path.append('../')
import numpy as np
import GenPulseClass
import matplotlib.pyplot as plt
import DigDiscClass
import WaveFormNoiser
from scipy.optimize import curve_fit

# Waveform parameters
# fsps = np.array([1.])
fsps = np.arange(1.,11.,0.5)
Nwaves = 10000
v0 = 0.
# v1 = np.arange(10.,110.,10.)
v1 = np.array([10.])
tdelay = 5.
# trise = np.arange(1.,11.,10.)
trise = np.array([10.])
ton = 10.
tfall = 10.
sigma_v = np.arange(0.1,1,0.1)
# sigma_v = np.array([.1])
vthr = 5.

ddc = DigDiscClass.DigDiscClass(vthr)
tdisc = np.zeros(Nwaves)

fout = open('out.txt','w')

sigma_t = np.zeros(len(sigma_v))
for n in range(len(fsps)):
    for m in range(len(v1)):
        for k in range(len(trise)):
            for j in range(len(sigma_v)):
                for i in range(Nwaves): 
                    # Horizontal array
                    wfn = WaveFormNoiser.WaveFormNoiser(sigma_v[j],fsps[n])
                    x = np.arange(0,20,1./fsps[n],dtype=float)
                    x = wfn.smear_t(x)
                    gpc = GenPulseClass.GenPulseClass(v0,v1[m],tdelay,trise[k],ton,tfall)
                    y = np.array([gpc.eval(xi) for xi in x])
                    y = wfn.smear_v(y)
                    tdisc[i] = ddc.disc(x,y)
                    # print tdisc[i]
                    # print x
                    # print y
                    # plt.plot(x,y,'o-')
                    # plt.show()
                mu = np.mean(tdisc)
                sigma = np.std(tdisc)
                sigma_t[j] = sigma
                print 'fsps = %f, v1 = %f, trise = %f, sigma_v = %f, sigma_t = %f' % (fsps[n],v1[m],trise[k],sigma_v[j],np.std(tdisc))
                # n, bins, patches = plt.hist(tdisc,1000,(0,100),normed=1)
                # plt.xlim(mu-4*sigma,mu+4*sigma)
                # plt.yscale('log')
                # plt.show()

        # Fit the curves
        def f(x,m,b): 
            return m*x + b

        popt,pcov = curve_fit(f,sigma_v[3:-1],sigma_t[3:-1])
        print popt
        plt.plot(sigma_v,sigma_t,'o-')
        plt.plot(sigma_v,f(sigma_v,popt[0],popt[1]),'r-')
        plt.show()

        strout = '%f,%f,%f,%f,%f\n' % (fsps[n],v1[m],trise[k],popt[0],popt[1])
        fout.write(strout)
