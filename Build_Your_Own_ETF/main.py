import pandas as pd
import requests
from get_all_tickers import get_tickers as gt

def url(symbol: str, key):
		return "https://financialmodelingprep.com/api/v3/market-capitalization/" + symbol + "?apikey=" + key

def market_cap(key,tickers):

	# Define lists of symbols and market caps
	symbols = []
	market_caps = []

	# DataFrame to store all the data
	data = pd.DataFrame(columns = ['Symbol', 'Market Cap'])

	# Iterate based on the symbols list and add to DataFrame
	for item in tickers:
		response = requests.get(url(symbol = item, key = key)).json()

		symbols.append(response[0]['symbol'])
		market_caps.append(response[0]['marketCap'])
    
	# Add data to the dataframe
	data['Symbol'] = symbols
	data['Market Cap'] = market_caps
	return data

def tickers():
	tickers = gt.get_tickers(AMEX=False)
	return tickers

def bus():
	#user input (defines which parameters to use)
	#something that runs the necessary modules
		#module() (gets list)
		#module(n)( gets list)(n)
	#returns final list
	#display list to user
	#
	#
	params = {'marketcap':100000000}
	key = 'e761f6394296ca70082ffacff21f4733'
	#
	threshold = params["marketcap"]*.2
	print(threshold)

	
	ticker_list = tickers()
	data = market_cap(key,tickers)



	print(data)

	

bus()