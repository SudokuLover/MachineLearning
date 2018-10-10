#Upper Confidence Band

#import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
dataset = pd.read_csv('ads_CTR_Optimisation.csv')

#using Random selection
import random
N=10000
d=10
ads_selected=[]
total_rewards=0
for n in range(0,N):
    ads=random.randrange(d)
    ads_selected.append(ads)
    rewards=dataset.values[n,ads]
    total_rewards=total_rewards + rewards
    
#Visualizing
plt.hist(ads_selected)
plt.title('Histogram of ads selection')
plt.xlabel('ads')
plt.ylabel('no of times each ads selected')
plt.show()