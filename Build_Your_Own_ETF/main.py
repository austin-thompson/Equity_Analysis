
	#version1
		#user input (defines which parameters to use)
		#something that runs the necessary modules
		#module() (gets list)
		#module(n)( gets list)(n)
		#returns final list
		#display list to user
	#version2
		# features
		# update gets all needed data without needing a key so as not to get blacklisted or timed-out
		#
#                     import
	import pandas as pd
	import numpy as np
	import requests
	import yfinance as yf
	from get_all_tickers import get_tickers as gt


#                     utils
	def update():
		tickers_all = gt.get_tickers(AMEX=False)
		tickers = yf.Tickers(tickers_all)
		df = pd.DataFrame(tickers)
		df.to_csv #to do: SAVE TO LOCATION
		return df
	def marketcap_module(df, params):
		# Iterate through df and assign CAP weight based on distmap from target
		for item in tickers:
			df.item = 
		return df
	def dividend_module(df, params):
		# Iterate through df and assign DIV weight based on distmap from target
		for item in tickers:
			df
		return df
	def price_to_earnings_module(df, params):
		# Iterate through df and assign PE weight based on distmap from target
		for item in tickers:
			# gaussiandist out from target applying outward
			# append new column
			df=df_with_weight
		return df
#                     algos & bus
	def controller(params, df):

		for item in params
			item.distmap = np.array[gaussiandist(len(df)]# define this based on gaussian dist
			item.weight_max =  item(1)*item(2)# this is target but formatted
			item.target  = item(1)# used in final solver
		df = module(df,params)
		df = price_to_earnings_module(df,params)
		df = dividend_module(df,params)

		# solver?????
	def solver(params, df):
		
#                     run
	def run():
	
		#                  input
		test_params = {'CAP':[100000000,6],'DIV':[.2,4],'PE':[60,10]}
		#                  update
		if csv_date != today
			df = update()
		else
		df = pd.read_csv("data.csv")

		#                 controller
		controller(params, df)
		# slover??

		return df

	

run()