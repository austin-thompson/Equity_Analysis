# File Name:
#
# Description:
#
#

####################################################################

#
# sys imports
#
import json
import pandas as pd
import pandas_datareader as web
import requests
from datetime import date
from IPython.display import display
import numpy as np

from enum import Enum
from enum import auto


####################################################################
#
# Description:
#  Returns metadata for a specific exchange
#   Available: US, NASDAQ, OTCBB, PINK, BATS
#
# TODO: look into better API, if one isn't found update
#        documentation
#
####################################################################
def get_exchange_data(key, exchange="NYSE"):
    # debug
    print("method: 'get_exchange_data' executing....")

    endpoint = f"https://eodhistoricaldata.com/api/exchange-symbol-list/"
    endpoint += f"{exchange}?api_token={key}&fmt=json"
    call = requests.get(endpoint).text
    exchange_data = pd.DataFrame(json.loads(call))

    # debug
    print("'get_exchange_data' completed!!!")

    return exchange_data


####################################################################
#
# Description:
#  TODO: Update method description
#
####################################################################
def fundamental_stock_data_by_exchange(exchange, analysis_params, default_params=[]):
    root_dir_location = "../../Utilities/Fundamental_Stock_Data_By_Exchange/"

    # csv parameters
    api_key = open(
        root_dir_location + "config/api_token.txt"
    ).read()  # define this api name better
    raw_data_location = root_dir_location + "csv/raw_data/raw_data.csv"
    result_set_location = (
        root_dir_location
        + "csv/result_set/result_set_"
        + exchange
        + "_"
        + str(date.today())
        + ".csv"
    )  # replace with formatted string

    print("Querying Exchange: " + exchange)
    print(
        "---------------------------------------------------------------------------------------------"
    )

    # change csv calls to leverage dataframes instead
    #### UNCOMMENT BELOW CODE FOR LIVE TICKER SYMBOL LIST GENERATION FOR SELECTED EXCHANGE
    # raw_data = get_exchange_data(api_key, exchange) #change api_key to better name above
    # raw_data.to_csv(raw_data_location, encoding="utf-8", index=False)
    # raw_data = pd.read_csv(raw_data_location)

    #### FOR TESTING PURPOSES TO AVOID EXCEEDING API CALLS FOR eodhistoricaldata.com
    raw_data = pd.read_csv(root_dir_location + "csv/raw_data/test_short_nasdaq.csv")

    list_of_ticker_symbols_by_exchange = list(raw_data["Code"])

    # print("BEFORE DELETE: ", list_of_ticker_symbols_by_exchange)

    running_total: int = 0
    end_total: int = len(list_of_ticker_symbols_by_exchange)

    market_data = []
    bad_tickers = []

    # queries yahoo finance for ticker passed, keeps track of bad pulls (ie. ticker lacking appropiate data)
    for ticker in list_of_ticker_symbols_by_exchange:
        running_total += 1
        try:
            temp_data = web.get_quote_yahoo(ticker)
            market_data.append(temp_data)
            print(
                "[" + str(running_total) + "/" + str(end_total) + "] Success with:",
                ticker,
            )
        except:
            print(
                "[" + str(running_total) + "/" + str(end_total) + "] Error with:",
                ticker,
            )
            bad_tickers.append(ticker)

    # culls tickers of tickers lacking appropiate data
    for ticker in bad_tickers:
        list_of_ticker_symbols_by_exchange.remove(ticker)

    # print("AFTER DELETE: ",list_of_ticker_symbols_by_exchange)

    # adds index column, inserts ticker symbols into dataframe, resets index
    df = pd.concat(market_data, axis=0)
    df.insert(0, "tickerSymbol", list_of_ticker_symbols_by_exchange)
    df.index = range(0, len(list_of_ticker_symbols_by_exchange), 1)

    # define params for analysis, scrubs data accordingly (ie. drops unnecessary columns)
    df = df.loc[:, analysis_params]

    # scrub data, removes rows with missing values
    for key in analysis_params:
        df[key].replace("", np.nan, inplace=True)

    # save data into csv format (replace with some form of database)
    # df.to_csv(result_set_location, encoding="utf-8", index=False)
    # print("Data Frame Successfully saved to:" , result_set_location)

    # display(df)

    # return a dataframe
    return df


####################################################################
#
# Description:
#  TODO: Update method description
#
####################################################################
def execute(exchange, analysis_params, default_params=[]):
    return fundamental_stock_data_by_exchange(exchange, analysis_params)
