
import json
import pandas as pd
import pandas_datareader as web
import requests
from datetime import date
from IPython.display import display

####################################################################

"""
returns metadata for a specific exchange
available: US, NASDAQ, OTCBB, PINK, BATS
"""
def get_exchange_data(key, exchange="NYSE"):
	endpoint = f"https://eodhistoricaldata.com/api/exchange-symbol-list/"
	endpoint += f"{exchange}?api_token={key}&fmt=json"
	
	print("get_exchange_data executing....")

	call = requests.get(endpoint).text
	exchange_data = pd.DataFrame(json.loads(call))
	

	print("get_exchange_data completed!!!")
	
	return exchange_data

####################################################################

"""
PLACEHOLDER
"""
def main():
	# parameters
	exchange = "NYSE"
	api_key = open("config/api_token.txt").read() # define this api name better
	raw_data_location = "csv/raw_data/raw_data.csv"
	result_set_location = "csv/result_set/result_set_" + exchange + "_" + str(date.today()) + ".csv" # replace with formatted string

	# change csv calls to leverage dataframes instead
	#### UNCOMMENT BELOW CODE FOR LIVE TICKER SYMBOL LIST GENERATION FOR SELECTED EXCHANGE
	raw_data = get_exchange_data(api_key, exchange) #change api_key to better name above
	raw_data.to_csv(raw_data_location, encoding="utf-8", index=False) 
	raw_data = pd.read_csv(raw_data_location)
	
	#### FOR TESTING PURPOSES TO AVOID EXCEEDING API CALLS FOR eodhistoricaldata.com
	# raw_data = pd.read_csv("csv/raw_data/test_short_nasdaq.csv") 

	list_of_ticker_symbols_by_exchange = list(raw_data["Code"])
	print("BEFORE DELETE: ", list_of_ticker_symbols_by_exchange)
	
	running_total : int = 0
	end_total : int = len(list_of_ticker_symbols_by_exchange)
	
	market_data = []
	bad_tickers = []

	for ticker in list_of_ticker_symbols_by_exchange:
		running_total += 1
		try: 
			temp_data = web.get_quote_yahoo(ticker)
			market_data.append(temp_data)
			print( "[" + str(running_total) + "/" + str(end_total) + "] Success with:", ticker)
		except:
			print( "[" + str(running_total) + "/" + str(end_total) + "] Error with:", ticker)
			bad_tickers.append(ticker)

	for ticker in bad_tickers:
		list_of_ticker_symbols_by_exchange.remove(ticker)

	print("AFTER DELETE: ",list_of_ticker_symbols_by_exchange)
	
	df=pd.concat(market_data, axis=0)
	df.insert(0, "tickerSymbol", list_of_ticker_symbols_by_exchange)
	df.index = range(0, len(list_of_ticker_symbols_by_exchange), 1)
	
	df = df.loc[:, ["tickerSymbol", "marketCap", "trailingAnnualDividendYield", "trailingPE"]]

	# df.to_csv(result_set_location, encoding="utf-8", index=False)

	# print("Data Frame Successfully saved to:" , result_set_location)
	display(df)

	return df

####################################################################

"""
PLACEHOLDER
"""
main()

####################################################################

