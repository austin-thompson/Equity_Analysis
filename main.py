import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from datetime import datetime
import mplfinance as mpf


# pulls ticker info, converts in csv
def ticker_info_csv_from_yahoo(ticker, startDate, endDate):
	start = datetime.fromisoformat(startDate)
	end = datetime.fromisoformat(endDate)

	print ('start: ' + str(start))
	print ('end: ' + str(end))
	df = web.DataReader(ticker, 'yahoo', start, end)

	df.to_csv('csv/' + ticker + '.csv')

	return df


# creates dataframe from csv file
def get_df_from_csv(ticker):
	try:
		df = pd.read_csv('csv/' + ticker + '.csv')
	except FileNotFoundError:
		print("File doesn't exist")
	else:
		return df



# adds return by day over user defined time
def add_daily_return_to_df(df, ticker):
	df['daily_return'] = (df['Adj Close'] / df['Adj Close'].shift(1)) - 1
	df.to_csv('csv/' + ticker + '.csv')

	return df

# gets percentage return over user defined time
def get_return_defined_time(df1, startDate, endDate):
	df1['Date'] = pd.to_datetime(df1['Date'])
	mask = (df1['Date'] > startDate) & (df1['Date'] <= endDate)
	daily_ret = df1.loc[mask]['daily_return'].mean()
	df2 = df1.loc[mask]
	days = df2.shape[0]
	return (days * daily_ret)


# draws Graphs
def mplfinance_plot(ticker, chartType, startDate, endDate):
	try:
		df = pd.read_csv('csv/' + ticker + '.csv')
	except FileNotFoundError:
		print("File doesn't exist")
	else:
		df.index = pd.DatetimeIndex(df['Date'])
		df_sub = df.loc[startDate:endDate]
		mpf.plot(df_sub, type=chartType)



		# mpf.plot(df_sub, type='candle')
		# mpf.plot(df_sub, type='line')
		# mpf.plot(df_sub, type='ohlc', mav=4)


		#  suppose to avg volume by day (not working)
		# s = mpf.make_mpf_style(base_mpf_style='charles', rc={'font.size': 8})
		# fig = mpf.figure(figsize=(12,8), style=s)
		# ax = fig.add_subplot(2,1,2)
		# av = fig.add_subplot(2,1,2, sharex=ax)
		# mpf.plot(df_sub, type=chartType, mav=(3,5,7), ax=ax, volume=av, show_nontrading=True)


# runs main Program
def run():

	# variables (make user defined)
	tickerSymbol = 'VOO'
	startDate = '2020-01-01'
	endDate = '2021-01-01'

	ticker_info_csv_from_yahoo(tickerSymbol, startDate, endDate)
	dataFrame = get_df_from_csv(tickerSymbol)
	add_daily_return_to_df(dataFrame, tickerSymbol)
	tot_ret = get_return_defined_time(dataFrame, startDate, endDate)

	print("Total Return:", tot_ret)

	mplfinance_plot(tickerSymbol, 'candle', startDate, endDate)

run()