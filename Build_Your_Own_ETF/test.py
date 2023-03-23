import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

params = {'CAP':[10,4],'DIV':[.2,3],'PE':[60,3]}
df = pd.DataFrame({'TKR':['MSFT','AAPL','NVDA','CGNX','TM'],'CAP': [4, 6, 30,15,10],'DIV':[0,.1,.05,.2,.5],'PE':[10,60,80,30,20]})



riskdist = [60,20,10]
print(riskdist[0])
