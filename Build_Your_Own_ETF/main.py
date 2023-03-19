#Build_Your_Own_ETF version3 
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
import requests
import yfinance as yf
from get_all_tickers import get_tickers as gt


#                     utils ****update()TO BE CHANGED*****
def update():
	tickers_all = gt.get_tickers(AMEX=False)
	tickers = yf.Tickers(tickers_all)
	df = pd.DataFrame
	for ticker in tickers:
		df.append(ticker.fast_info)
	df.to_csv #to do: SAVE TO LOCATION
	return df
def param_module(dist, target_index):
		# Iterate through df and assign PE weight based on distmap from target
	column_weight = []
	dist_middle = len(dist)/2
	for item in len(dist):
		weight_score = dist[abs(dist_middle - abs(item.index.item() - target_index))]
			# gaussiandist out from target applying outward
			# append new column
		column_weight.append(weight_score)
	return column_weight
#                     algos & bus
def normal_dist(x,mean,sd):
	prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
	return prob_density

def controller(params, df):
	df.index.size
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
		distmap = (distmap/df_length)*weight_max
	#			target_idx = index
		target_df = df[df.param == 2]
		if target_df.index.size == 1:
			target_idx = target_df.param.index.item()
		else:
			target_idx = round(np.median(target_df.param.index.values))		
	#			calls param module
			param_column = param_module(distmap,target_idx)# centers dist map to target while keeping length of column len(df)
			df.insert(df.columns.size-1, param+"W", param_column)
		return df

	def solver(df, riskdist, budget):

		for item in riskdist:
			(item*budget)/df.(itemno).price=shares #calc shares
			shares_column.append(shares) #add column with shares
		df.append(shares_column)
		df.column.sort(desc) 
		for item in df:
			if item.shares >=1:
				etf_column = item.allinfo()
			else:
				break
		return etf_column

		#output is df of length len(dist) ordered by shares	
#                     run
	def run():
	
		#                  input
		test_params = {'CAP':[100000000,4],'DIV':[.2,3],'PE':[60,3]}
		#                  update
		if csv_date != today:
			df = update()
		else:
			df = pd.read_csv("data.csv")

		#                 controller
		#make params a dataframe
		df = controller(params, df)
		riskdist = [60,20,10,5,2.5,2.5]
		budget = 10000
		etf_column = solver(df,riskdist,budget)

		return etf_column

	

run()