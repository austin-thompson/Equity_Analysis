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
import requests
from icecream import ic


apiBase = "https://query2.finance.yahoo.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}


def getCredentials(
    cookieUrl="https://fc.yahoo.com", crumbUrl=apiBase + "/v1/test/getcrumb"
):
    cookie = requests.get(cookieUrl).cookies
    crumb = requests.get(url=crumbUrl, cookies=cookie, headers=headers).text
    return {"cookie": cookie, "crumb": crumb}


def quote(symbols, credentials):
    url = apiBase + "/v7/finance/quote"
    params = {"symbols": ",".join(symbols), "crumb": credentials["crumb"]}
    response = requests.get(
        url, params=params, cookies=credentials["cookie"], headers=headers
    )
    quotes = response.json()["quoteResponse"]["result"]
    return quotes


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

    #### UNCOMMENT BELOW CODE FOR LIVE TICKER SYMBOL LIST GENERATION FOR SELECTED EXCHANGE (20 Calls a Day....)
    # raw_exchange_data = get_all_tickers_in_exchange(api_key, exchange)
    # database_csv_filepath = "fundamental_stock_data" + "_" + exchange + ".csv"

    #### FOR TESTING PURPOSES TO AVOID EXCEEDING API CALLS FOR eodhistoricaldata.com
    raw_exchange_data = pd.read_csv(util_dir_path + "testing_data/nyse_test_short.csv")
    database_csv_filepath = "testing_fundamental_stock_data" + "_" + exchange + ".csv"

    list_of_ticker_symbols = list(raw_exchange_data["Code"])

    print(list_of_ticker_symbols)

    credentials = getCredentials()

    # queries yahoo finance for ticker passed, keeps track of bad pulls (ie. ticker lacking appropiate data)
    # TODO: Figure out why 'quote()' throws an error when it pulls on a "bad" ticker
    #        might make sense to change this to only do one ticker at a time, see old commit
    fundamental_stock_data = quote(list_of_ticker_symbols, credentials)

    # adds index column, inserts ticker symbols into dataframe, resets index
    df_fundamental_stock_data = pd.DataFrame(fundamental_stock_data)
    df = pd.concat([df_fundamental_stock_data], axis=0)
    # df.insert(0, "tickerSymbol", list_of_ticker_symbols)
    # df.index = range(0, len(list_of_ticker_symbols), 1)

    # replaces missing data with NaN
    for key in df.keys():
        df[key].replace("", np.nan, inplace=True)

    # save data into csv format
    df.to_csv(database_csv_filepath, encoding="utf-8", index=False)
    print("Data Frame Successfully saved to:", database_csv_filepath)

    # # ** DEBUG **
    display(df)


####################################################################
# Description:
#  TODO: Update method description
####################################################################
def execute(exchange):
    get_fundamental_stock_data_by_exchange(exchange)
