import numpy as np
import matplotlib.pyplot as plt
import csv

################################################
#
# Tyler Anderson
# Sun May 20 17:18:03 EDT 2018
#
# Read in ASCII data from oscilloscope
#
################################################

def read_scope(fname=''): 
    # print fname
    fin = open(fname,'r')
    reader = csv.reader(fin,delimiter=' ')
    for i in range(5): 
        header = reader.next()
        # print header
        
    v = np.array([])
    t = np.array([])
    for row in reader: 
        t = np.append(t,1.E9*float(row[0]))
        v = np.append(v,1000.*float(row[1]))
    
    fin.close()
    return t,v
    

