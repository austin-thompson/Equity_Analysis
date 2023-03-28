import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from etfbuilder import *
keys_include = ["longName","marketCap","trailingPE","trailingAnnualDividendYield","price","ytdReturn"]
#       trim df
params = {'marketCap':[1000000000,4],'trailingAnnualDividendYield':[1,3],'trailingPE':[30,3]}
df = load_market()
keys = df.keys()
for key, values in df.items():
    if key not in keys_include:
        df.pop(key)
riskdist = [.6,.25,.15,0,0]
budget = 1000000
# objective: call score() with grab ticker data as input and params as input
print(score(params,df,riskdist,budget))
