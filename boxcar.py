###############################################################################################
# Box car averager
import numpy as np

def boxcar(t,v,n): 
    if(n==0): 
        return t,v
    v1 = np.zeros(len(v)-n)
    t1 = np.zeros(len(t)-n)
    for i in range(len(v1)): 
        vsum = 0
        for j in range(n): 
            vsum += v[n+i-j]
        v1[i]=float(vsum)/float(n)
        t1[i] = t[i]
        # print i-n+1
    # sys.exit()    
    return t1,v1

