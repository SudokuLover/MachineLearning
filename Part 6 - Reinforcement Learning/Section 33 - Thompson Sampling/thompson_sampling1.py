#Thomson Sampling

#import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
dataset = pd.read_csv('ads_CTR_Optimisation.csv')

#implementing Thomson Sampling
import random
N=10000
d=10
ads_selected=[]
number_of_rewards_1=[0]*d
number_of_rewards_0=[0]*d
total_rewards=0

for n in range(0,N):
    ad=0
    max_random=0
    for i in range(0,d):
        random_beta=random.betavariate(number_of_rewards_1[i]+1,number_of_rewards_0[i]+1)
        if(random_beta>max_random):
            max_random=random_beta
            ad=i
    ads_selected.append(ad)
    rewards=dataset.values[n,ad]
    if rewards==1:
        number_of_rewards_1[ad]=number_of_rewards_1[ad]+1
    else:
        number_of_rewards_0[ad]=number_of_rewards_0[ad]+1
    total_rewards=total_rewards + rewards

        
    
#Visualizing
plt.hist(ads_selected)
plt.title('Histogram of ads selection')
plt.xlabel('ads')
plt.ylabel('no of times each ads selected')
plt.show()