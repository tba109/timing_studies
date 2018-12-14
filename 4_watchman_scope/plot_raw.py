import numpy as np
import matplotlib.pyplot as plt

for i in range(1000):
        fin = open('/media/tyler/Seagate Expansion Drive/20181212_watchman_spe/C2--waveforms--%05d.txt' % i)
	print i
	# Header
	for j in range(5): 
		fin.readline()
	x = []
	y = []
	for line in fin: 
		x.append(float(line.split(',')[0]))
		y.append(float(line.split(',')[1]))
	plt.plot(x,y)
        plt.ylim(-0.0250,-0.005)
	plt.show()
        fin.close()
	
