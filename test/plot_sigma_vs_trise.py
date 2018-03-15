import matplotlib.pyplot as plt

fin = open('out_high_stat_sigmat_vs_t.txt','r')

x = []
sigma_t = []
for line in fin: 
    x.append(float(line.split(',')[0]))
    sigma_t.append(float(line.split(',')[1]))

print x
print sigma_t

fin.close()

plt.plot(x,sigma_t,'o-')
plt.xlabel('Rise Time (ns)')
plt.ylabel('Timing Resolution (ns)')
plt.show()
