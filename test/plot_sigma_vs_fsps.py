import matplotlib.pyplot as plt

fin = open('out.txt','r')

x = []
sigma_t = []
for line in fin: 
    x.append(float(line.split(',')[0]))
    sigma_t.append(float(line.split(',')[3]))

print x
print sigma_t

fin.close()

plt.plot(x,sigma_t,'o-')
plt.xlabel('Sample Rage (GSPS)')
plt.ylabel('Timing Resolution (ns)')
plt.show()
