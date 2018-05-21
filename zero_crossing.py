def zero_crossing(t,v,thr=0.25): 
    i=0
    peaking = False
    for ti,vi in zip(t,v): 
        if(vi > thr):
            peaking = True
        if(peaking == True and vi < 0):
            break
        i+=1
    if(i==0): 
        tz = 0
    elif(i > len(t)-1): 
        return t[-1]
    else: 
        tz = t[i-1] - ((t[i] - t[i-1])/(v[i] - v[i-1]))*(v[i-1])
        # tz = t[i] + ((t[i+1] - t[i])/(v[i+1] - v[i]))*(v[i])
        # print t[i-1], t[i], v[i-1], v[i]
    return tz
