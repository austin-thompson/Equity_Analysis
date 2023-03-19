import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

params = {'CAP':[10,4],'DIV':[.2,3],'PE':[60,3]}
df = pd.DataFrame({'TKR':['MSFT','AAPL','NVDA','CGNX','TM'],'CAP': [4, 6, 30,15,12],'DIV':[0,.1,.05,.2,.5],'PE':[10,60,80,30,20]})


def normal_dist(x,mean,sd):
	prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
	return prob_density
param = 'CAP'
targetvalue = params[param][0]
weight_max =  params[param][1]# this is target but formatted
df_length = len(df)*2
x = np.linspace(1,df_length,df_length)
mean = np.mean(x)
sd = np.std(x)
    #Apply function to the data.
distmap = normal_dist(x,mean,sd)
distmap = (distmap/df_length)*weight_max
target_df = df[df.param == 2]
if target_df.index.size == 1:
    target_idx = target_df.param.index.item()
else:
    target_idx = round(np.median(target_df.param.index.values))		
#			calls param module
# Iterate through df and assign PE weight based on distmap from target
column_weight = []
dist_middle = len(dist)/2
for item in len(dist):
    weight_score = dist[abs(dist_middle - abs(item.index.item() - target_index))]
        # gaussiandist out from target applying outward
        # append new column
    column_weight.append(weight_score)
param_column = param_module(distmap,target_idx)# centers dist map to target while keeping length of column len(df)
df.insert(df.columns.size-1, param+"W", param_column)