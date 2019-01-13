import matplotlib.pyplot as plt

def zero_crossing_pos(t,v,thr=0.25): 
    i=0
    for i in range(len(v)):
        if v[i] <= thr:
            break
        i+=1
    j = 0
    for j in range(i,len(v)): 
        if(v[j] > 0): 
            break
        j+=1
    i = j
    m = (t[i] - t[i-1])/(v[i] - v[i-1])
    b = t[i-1] - m*v[i-1]
    tz = b
    if False:
        print t[i-1], t[i], v[i-1], v[i]
        print tz*1.E9
        plt.plot(t,v,'-o')
        plt.axvline(tz)
        plt.axhline(0)
        ytz = [ti/m - b/m for ti in t]
        plt.plot(t,ytz)
        plt.ylim(-0.005,0.005)
        plt.show()
    if(i==0): 
        tz = 0
    elif(i > len(t)-1): 
        return t[-1]
    return tz
