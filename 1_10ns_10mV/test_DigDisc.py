import sys
sys.path.append('../')
import numpy as np
import GenPulseClass
import matplotlib.pyplot as plt
import DigInterpClass
import DigDiscClass
import WaveFormNoiser
from scipy.optimize import curve_fit
from ROOT import TH1F

# Waveform parameters
# fsps = np.array([1.])
# fsps = np.arange(1.,11.,0.5)
fsps = [100.]
Nwaves = 10000
v0 = 0.
# v1 = np.arange(10.,110.,10.)
v1 = np.array([10.])
tdelay = 5.
# trise = np.arange(1.,11.,1.)
trise = np.array([10.])
ton = 10.
tfall = 10.
sigma_v = np.arange(0.1,1,0.1)
# sigma_v = np.arange(0.001,.01,0.001)
# sigma_v = np.array([.1])
vthr = 5.

ddc = DigDiscClass.DigDiscClass(vthr)
dic = DigInterpClass.DigInterpClass(vthr,20.)

fout = open('out.txt','w')

tdisc_method = 'ddc'
# tdisc_method = 'dic'

plot_wv = True
# plot_wv = False

# Fit the curves
def f(x,m,b): 
    return m*x + b

sigma_t = np.zeros(len(sigma_v))
for n in range(len(fsps)):
    for m in range(len(v1)):
        for k in range(len(trise)):
            for j in range(len(sigma_v)):
                tdisc = np.zeros(Nwaves)
                h1 = TH1F("h1","",1000,4.9,5.1)
                for i in range(Nwaves): 
                    # Horizontal array
                    wfn = WaveFormNoiser.WaveFormNoiser(sigma_v[j],fsps[n])
                    x = np.arange(0,20,1./fsps[n],dtype=float)
                    x = wfn.smear_t(x) # Note: comment this line to turn off time smearing
                    gpc = GenPulseClass.GenPulseClass(v0,v1[m],tdelay,trise[k],ton,tfall)
                    y = np.array([gpc.eval(xi) for xi in x])
                    y = wfn.smear_v(y)
                    # ddc
                    if tdisc_method == 'ddc': 
                        tdisc[i] = ddc.disc(x,y)
                        if plot_wv: 
                            print tdisc[i]
                            plt.plot(x,y,'o-')
                            plt.axhline(y=ddc.vthr,color='r')
                            plt.show()
                    # dic
                    if tdisc_method == 'dic': 
                        # popt = dic.disc_interp(x,y)
                        # tdisc[i] = -popt[1]/popt[0]
                        tdisc[i] = dic.disc_interp(x,y)
                        if plot_wv: 
                            print tdisc[i]
                            plt.plot(x,y,'o-')
                            plt.axhline(y=dic.vthr,color='r')
                            # plt.plot(x,f(x,popt[0],popt[1]),'g-')
                            plt.show()
                    # h1.Fill(tdisc[i])
                mu = np.mean(tdisc)
                sigma = np.std(tdisc)
                sigma_t[j] = sigma
                print 'fsps = %f, v1 = %f, trise = %f, sigma_v = %f, sigma_t = %f' % (fsps[n],v1[m],trise[k],sigma_v[j],sigma)
                plt.hist(tdisc,100)
                plt.show()
                # h1.Draw()
                # raw_input()
                # h1.Delete()
            popt,pcov = curve_fit(f,sigma_v[3:-1],sigma_t[3:-1])
            strout = '%f,%f,%f,%f,%f\n' % (fsps[n],v1[m],trise[k],popt[0],popt[1])
            print strout
            plt.plot(sigma_v,sigma_t,'o-')
            plt.plot(sigma_v[3:-1],f(sigma_v[3:-1],popt[0],popt[1]),'r-')
            plt.show()
            fout.write(strout)
fout.close()
