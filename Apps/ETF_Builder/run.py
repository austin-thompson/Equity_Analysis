####################################################################
# File Name:
#
# Description:
#
#
####################################################################

#
# sys imports
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from etf_builder import *
from IPython.display import display

# clean up this implementation (create pip modules?)
# START
#
# local imports
#
import sys

sys.path.append("../../Utils")
from Fundamental_Stock_Data_By_Exchange import fundamental_stock_data_by_exchange

# END


####################################################################
#
# Description:
#  TODO: Update method description
#
####################################################################
def execute():
    exchange = "NASDAQ"
    analysis_params = [
        "quoteType",
        "tickerSymbol",
        "longName",
        "marketCap",
        "trailingPE",
        "trailingAnnualDividendYield",
        "price",
    ]

    user_defined_params = {
        "marketCap": [1000000000, 4],
        "trailingAnnualDividendYield": [1, 3],
        "trailingPE": [30, 3],
    }

    df = fundamental_stock_data_by_exchange.execute(exchange, analysis_params)

    risk_dist = [0.6, 0.25, 0.15, 0, 0]
    budget = 1000000

    print(
        "---------------------------------------------------------------------------------------------"
    )

    print("params: " + str(user_defined_params))
    print("budget: " + str(budget))

    print(
        "---------------------------------------------------------------------------------------------"
    )

    # # objective: call score() with grab ticker data as input and params as input
    print(score(user_defined_params, df, risk_dist, budget))


# Executes Build Your Own ETF
execute()
