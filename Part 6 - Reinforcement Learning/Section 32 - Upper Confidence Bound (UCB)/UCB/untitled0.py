import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')


#UCB
import math
N = 10000
d = 10
c = []
a = [0] * d
b = [0] * d
totalreward = 0
for n in range(0,N):
    ad = 0
    maxub = 0
    for i in range (0,d):
                             if (a[i]>0):
                              avg = a[i] / b[i]
                               delta_i = math.sqrt(3/2 * math.log(n+1) / a)
                               upperbound = avg + delta_i
            else:
                           upperbound = 1e400
            if upperbound  > maxub:
             maxub = upperbound
             ad = i
 c.append(ad)
 a[ad] = a[ad] + 1
 reward = dataset.values[n,ad]
 b[ad] = b[ad] + reward
 totalreward = totalreward + reward
     