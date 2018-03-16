import matplotlib.pyplot as plt
fin = open('disc_fs.txt','r')

x_disc = []
sigma_t_disc = []
for line in fin: 
    x_disc.append(float(line.split(',')[0]))
    sigma_t_disc.append(float(line.split(',')[3]))

fin.close()

plt.plot(x_disc,sigma_t_disc,'o-')
plt.xlabel('Sample Rate (GSPS)')
plt.ylabel('Timing Resolution (ns)')
plt.show()

fin = open('interp_fs.txt','r')

x_interp = []
sigma_t_interp = []
for line in fin: 
    x_interp.append(float(line.split(',')[0]))
    sigma_t_interp.append(float(line.split(',')[3]))

fin.close()

plt.plot(x_interp,sigma_t_interp,'o-')
plt.xlabel('Sample Rate (GSPS)')
plt.ylabel('Timing Resolution (ns)')
plt.show()

# Comparison plot
plt.plot(x_disc,sigma_t_disc,'o-',color='b')
plt.plot(x_interp,sigma_t_interp,'o-',color='r')
plt.xlabel('Sample Rate (GSPS)')
plt.ylabel('Timing Resolution (ns)')
plt.show()
