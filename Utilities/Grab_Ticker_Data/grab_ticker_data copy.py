
import json
import pandas as pd
import requests
import yfinance as yf

# Define a function to get the url based on your API key and 
def url(symbol: str, api_key):
	return "https://financialmodelingprep.com/api/v3/market-capitalization/" + symbol + "?apikey=" + api_key


"""
returns metadata for a specific exchange
available: US, NASDAQ, OTCBB, PINK, BATS
"""
def get_exchange_data(key, exchange='NYSE'):
	endpoint = f"https://eodhistoricaldata.com/api/exchange-symbol-list/"
	endpoint += f"{exchange}?api_token={key}&fmt=json"
	
	print("get_exchange_data executing....")

	call = requests.get(endpoint).text
	exchange_data = pd.DataFrame(json.loads(call))
	

	print("get_exchange_data completed!!!")
	
	return exchange_data




"""
PLACEHOLDER
"""
def main():
	exchange = "NYSE"
	# api_key = open('config/api_token.txt').read() # define this api name better
	FMP_key = 'e761f6394296ca70082ffacff21f4733' # put in config file

	# Define lists of symbols and market caps
	symbols = []
	market_caps = []

	# raw_data = get_exchange_data(api_key, exchange) #change api_key to better name above
	# raw_data.to_csv("test.csv", encoding='utf-8', index=False) # change test.csv to file_location

	raw_data = pd.read_csv('test_short.csv') # change to file_location
	list_of_ticker_symbols_by_exchange = list(raw_data['Code'])
	print(list_of_ticker_symbols_by_exchange)


	# All the symbols you want the data for
	all_symbols = ['AAPL', 'MSFT', 'NFLX', 'NVDA', 'FB', 'TWTR', 'TSLA', 'AMZN', 'WMT']

	print(all_symbols)

	all_symbols = list_of_ticker_symbols_by_exchange
	

	# DataFrame to store all the data
	data = pd.DataFrame(columns = ['Symbol', 'Market Cap'])

	# Iterate based on the symbols list and add to DataFrame
	for item in all_symbols:
		response = requests.get(url(symbol = item, api_key = FMP_key)).json()

		if response != []:
			print(response)

			symbols.append(response[0]['symbol'])
			market_caps.append(response[0]['marketCap'])
		
	# Add data to the dataframe
	data['Symbol'] = symbols
	data['Market Cap'] = market_caps

	print(data)


"""
PLACEHOLDER
"""
main()


