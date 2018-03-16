import matplotlib.pyplot as plt
fin = open('disc_risetime.txt','r')

x_disc = []
sigma_t_disc = []
for line in fin: 
    x_disc.append(float(line.split(',')[2]))
    sigma_t_disc.append(float(line.split(',')[3]))

fin.close()

plt.plot(x_disc,sigma_t_disc,'o-')
plt.xlabel('Rise Time (ns)')
plt.ylabel('Timing Resolution (ns)')
plt.show()

fin = open('interp_risetime.txt','r')

x_interp = []
sigma_t_interp = []
for line in fin: 
    x_interp.append(float(line.split(',')[2]))
    sigma_t_interp.append(float(line.split(',')[3]))

fin.close()

plt.plot(x_interp,sigma_t_interp,'o-')
plt.xlabel('Rise Time (ns)')
plt.ylabel('Timing Resolution (ns)')
plt.show()

# Comparison plot
plt.plot(x_disc,sigma_t_disc,'o-',color='b')
plt.plot(x_interp,sigma_t_interp,'o-',color='r')
plt.xlabel('Rise Time (ns)')
plt.ylabel('Timing Resolution (ns)')
plt.show()
