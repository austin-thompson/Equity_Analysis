####################################################################
# File Name:
#
# Description:
#
#
####################################################################

####################################################################
# Sys Imports
####################################################################
import numpy as np
import pandas as pd
import pandas_datareader as web
import json
import requests
from IPython.display import display
from alive_progress import alive_bar


####################################################################
# Description:
#  Returns metadata for a specific exchange
#   Available: US, NASDAQ, OTCBB, PINK, BATS
#
# TODO: look into better API, if one isn't found update
#        documentation
####################################################################
def get_all_tickers_in_exchange(api_key, exchange="NYSE"):
    #### ** DEBUG **
    print("method: 'get_all_tickers_in_exchange' executing....")

    end_point = f"https://eodhistoricaldata.com/api/exchange-symbol-list/"
    end_point += f"{exchange}?api_token={api_key}&fmt=json"
    api_call = requests.get(end_point).text
    exchange_data = pd.DataFrame(json.loads(api_call))

    #### ** DEBUG **
    print("method: 'get_all_tickers_in_exchange' completed!!!")

    return exchange_data


####################################################################
# Description:
#  TODO: Update method description
####################################################################
def get_fundamental_stock_data_by_exchange(exchange):
    util_dir_path = "../../Utils/Get_Fundamental_Stock_Data_By_Exchange/"

    api_key = open(util_dir_path + "util_config/api_key.txt").read()

    print("Querying Exchange: " + exchange)
    print(
        "---------------------------------------------------------------------------------------------"
    )

    #### UNCOMMENT BELOW CODE FOR LIVE TICKER SYMBOL LIST GENERATION FOR SELECTED EXCHANGE
    # raw_exchange_data = get_all_tickers_in_exchange(api_key, exchange)
    # database_csv_filepath = "fundamental_stock_data" + "_" + exchange + ".csv"

    #### FOR TESTING PURPOSES TO AVOID EXCEEDING API CALLS FOR eodhistoricaldata.com
    raw_exchange_data = pd.read_csv(
        util_dir_path + "testing_data/nasdaq_test_short.csv"
    )
    database_csv_filepath = "testing_fundamental_stock_data" + "_" + exchange + ".csv"

    list_of_ticker_symbols = list(raw_exchange_data["Code"])

    #### ** DEBUG **
    # print("BEFORE DELETE: ", list_of_ticker_symbols)

    fundamental_stock_data = []
    bad_ticker_symbols = []

    # queries yahoo finance for ticker passed, keeps track of bad pulls (ie. ticker lacking appropiate data)
    with alive_bar(
        len(list_of_ticker_symbols), bar="filling", spinner="dots_waves2"
    ) as bar:
        for individual_ticker_symbol in list_of_ticker_symbols:
            try:
                individual_ticker_symbol_data = web.get_quote_yahoo(
                    individual_ticker_symbol
                )
                fundamental_stock_data.append(individual_ticker_symbol_data)
                bar()
            except:
                bad_ticker_symbols.append(individual_ticker_symbol)
                bar()

    # culls tickers of those lacking appropiate data
    for individual_bad_ticker_symbol in bad_ticker_symbols:
        list_of_ticker_symbols.remove(individual_bad_ticker_symbol)

    #### ** DEBUG **
    # print("AFTER DELETE: ", list_of_ticker_symbols)

    # adds index column, inserts ticker symbols into dataframe, resets index
    df = pd.concat(fundamental_stock_data, axis=0)
    df.insert(0, "tickerSymbol", list_of_ticker_symbols)
    df.index = range(0, len(list_of_ticker_symbols), 1)

    # replaces missing data with NaN
    for key in df.keys():
        df[key].replace("", np.nan, inplace=True)

    # save data into csv format
    df.to_csv(database_csv_filepath, encoding="utf-8", index=False)
    print("Data Frame Successfully saved to:", database_csv_filepath)

    #### ** DEBUG **
    # display(df)


####################################################################
# Description:
#  TODO: Update method description
####################################################################
def execute(exchange):
    get_fundamental_stock_data_by_exchange(exchange)
