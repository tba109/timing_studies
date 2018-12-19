import numpy as np
import matplotlib.pyplot as plt
import sys

Nloops = 10
show_plot = False
Y_FFT_AVG = []

###################################################################
# Now plot impulse response
n2 = np.arange(-2000,2000,1)
fc = 0.005
h = [np.sin(2*np.pi*fc*n2i)/(n2i*np.pi) for n2i in n2]
plt.plot(h)
plt.show()

H_FFT = np.fft.fft(h)
MAG_H_FFT = [abs(IH) for IH in H_FFT[0:(len(n2)/2-1)]]
plt.plot(MAG_H_FFT)
# plt.xscale('log')
plt.show()

###################################################################
# Plot the filtered response
for i in range(Nloops):
    fin = open('/media/tyler/Seagate Expansion Drive/20181212_watchman_spe/C2--waveforms--%05d.txt' % i)
    print i
    # Header
    for j in range(5):
        fin.readline()
        n = [] 
        x = []
        y = []
        ni = 0
    for line in fin:
        n.append(ni)
	x.append(float(line.split(',')[0]))
	y.append(float(line.split(',')[1]))
        ni+=1
        y2 = np.convolve(y,h)
    fin.close()
    # plt.plot(x,y)
    # plt.plot(x,y2)
    plt.plot(y2)
    plt.show()
