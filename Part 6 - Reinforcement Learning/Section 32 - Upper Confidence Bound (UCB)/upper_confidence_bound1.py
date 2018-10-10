#Upper Confidence Band

#import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
dataset = pd.read_csv('ads_CTR_Optimisation.csv')

#implementing UCB
import math
N=10000
d=10
ads_selected=[]
number_of_selections=[0]*d
sum_of_rewards=[0]*d
total_rewards=0

for n in range(0,N):
    ad=0
    max_upper_bound=0
    for i in range(0,d):
        if(number_of_selections[i]>0):
            average_rewards=sum_of_rewards[i]/number_of_selections[i]
            delta_i=math.sqrt(3/2*math.log(n+1)/number_of_selections[i])
            upper_bound=average_rewards+delta_i
            
        else :
            upper_bound=1e400
        
        if(upper_bound>max_upper_bound):
            max_upper_bound=upper_bound
            ad=i
    ads_selected.append(ad)
    number_of_selections[ad]=number_of_selections[ad]+1
    rewards=dataset.values[n,ad]
    sum_of_rewards[ad]=sum_of_rewards[ad]+rewards
    total_rewards=total_rewards + rewards

        
    
#Visualizing
plt.hist(ads_selected)
plt.title('Histogram of ads selection')
plt.xlabel('ads')
plt.ylabel('no of times each ads selected')
plt.show()