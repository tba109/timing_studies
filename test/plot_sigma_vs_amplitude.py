import matplotlib.pyplot as plt

fin = open('out_high_stat_sigmat_vs_v1.txt','r')
# fin = open('out_high_stat_sigmat_vs_fixed_slew.txt','r')

x = []
sigma_t = []
for line in fin: 
    x.append(1./float(line.split(',')[0]))
    sigma_t.append(float(line.split(',')[2]))

print x
print sigma_t

fin.close()

plt.plot(x,sigma_t,'o-')
plt.xlabel('1/amplitude')
plt.ylabel('Timing Resolution (ns)')
plt.show()
