import matplotlib.pyplot as plt

fin = open('out.txt','r')

x = []
sigma_t = []
for line in fin: 
    x.append(float(line.split(' ')[0]))
    sigma_t.append(float(line.split(',')[3]))

print x
print sigma_t

fin.close()

# sigma_t2 = [st - 0.06 for st in sigma_t]

plt.plot(x,sigma_t,'o-')
plt.xlabel('Sample Rage (GSPS)')
plt.ylabel('Timing Resolution (ns)')
# plt.semilogy(1)
plt.show()
