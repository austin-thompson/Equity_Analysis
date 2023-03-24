import pandas as pd
import pandas_datareader as web
df = pd.DataFrame({'TKR':['MSFT','AAPL','NVDA','CGNX','TM'],'CAP': [4, 6, 30,15,10],'DIV':[0,.1,.05,.2,.5],'PE':[10,60,80,30,20],'PRICE':[50,60,80,30,20]})

print(df)

