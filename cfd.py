###############################################################################################
# Constant fraction discriminator
def cfd(t,x,d=1): 
    
    # Differentiate
    x2 = [xi - xj for xi,xj in zip(x[:-1*d],x[d:])]
    t2 = t[d:]
    
    return t2,x2
