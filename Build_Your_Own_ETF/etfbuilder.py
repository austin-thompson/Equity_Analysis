#Build_Your_Own_ETF version1 
		# progress notes
			# controller: calls param module, creates vector based on a normal gauss dist thats scaled to the input magnitude 
				#notes: close to complete the creation of the dist vector has been tested
				#need to finish and test param module before end to end testing can be done
			# param module: frame work done but not tested or completed
				#need to unit test assigning dist values based on the index difference provided by controller
				#need to create sample inpur params to unit test
			# update: need to incorporate austins progress
			# solver: 
#                     import
import pandas as pd
import numpy as np
# import requests
import yfinance as yf
# from get_all_tickers import get_tickers as gt
#                     utils ****update()TO BE CHANGED*****
def update():
	tickers_all = gt.get_tickers(AMEX=False)
	tickers = yf.Tickers(tickers_all)
	df = pd.DataFrame
	for ticker in tickers:
		df.append(ticker.fast_info)
	df.to_csv #to do: SAVE TO LOCATION
	return df
def param_module(distmap, target_idx):
#			******param module test******
# Iterate through df and assign PE weight based on distmap from target
	column_weight = []
	dist_middle = len(distmap)/2

	for indexdf in range(int(dist_middle)):
		weight_score = distmap[abs(int(dist_middle) - abs(indexdf - target_idx))]
			# gaussiandist out from target applying outward
			# append new column
		column_weight.append(weight_score)
	return column_weight
def score_module(params,df):
#			******param module test******
# Iterate through df and assign PE weight based on distmap from target
	column_score = []
	for indexdf in range(len(df)):
		score = 0
		for param in params:
			score += df.at[indexdf,param+"W"]
			# add param+W
			# append new column
		column_score.append(score)
	return column_score
#                     algos 
def normal_dist(x,mean,sd):
	prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
	return prob_density

def controller(params, df):
	scale_size = len(df)*2
	for param in params:
		targetvalue = params[param][0]
		weight_max =  params[param][1]# this is target but formatted
		df_length = len(df)*2
	#			distmap = [gauss*W]
		x = np.linspace(1,df_length,df_length)
			#Creating a Function.
		
			#Calculate mean and Standard deviation.
		mean = np.mean(x)
		sd = np.std(x)
			#Apply function to the data.
		distmap = normal_dist(x,mean,sd)
		distmap = (distmap/scale_size)*weight_max
		df = df.sort_values(by=[param])
		df = df.reset_index(drop=True)
		target_df = df.iloc[(df[param]-targetvalue).abs().argsort()[:2]] # finds target index(s)
		# gets single index or takes the median index
		if target_df.index.size == 1:
			target_idx = target_df[param].index.item()
		else:
			target_idx = round(np.median(target_df[param].index.values))		
	#			calls param module
		param_column = param_module(distmap,target_idx)# centers dist map to target while keeping length of column len(df)
		df.insert(df.columns.size-1, param+"W", param_column)

	score_column = score_module(params,df)
	df.insert(df.columns.size-1, "SCORE", score_column)

	return df

def solver(df, riskdist, budget):
	df = df.sort_values(by=['SCORE'],ascending=False)
	df = df.reset_index(drop=True)
	shares_column = []
	for idx in range(len(riskdist)):
		shares = (riskdist[idx]*budget)/df.at[idx,"price"] #calc shares
		shares_column.append(shares) #add column with shares
	for idx in range(len(df)-len(riskdist)):
		shares_column.append(0)
	df.insert(df.columns.size-1, "SHARES", shares_column)
	# df = df.sort_values(by=['SHARES'])
	# df = df.reset_index(drop=True)
	return df

		#output is df of length len(dist) ordered by shares	
#                     run
def score(params,df,riskdist,budget):
	#                  input
	# params = {'CAP':[10,4],'DIV':[.2,3],'PE':[60,3]}
	# df = pd.DataFrame({'TKR':['MSFT','AAPL','NVDA','CGNX','TM'],'CAP': [4, 6, 30,15,10],'DIV':[0,.1,.05,.2,.5],'PE':[10,60,80,30,20],'PRICE':[50,60,80,30,20]})
	# riskdist = [.6,.25,.15,0,0]
	# budget = 10000
	df = controller(params, df)	
	etf_column = solver(df,riskdist,budget)
	return etf_column
def load_market():
	df = pd.read_csv('EXAMPLE.csv')
	return df