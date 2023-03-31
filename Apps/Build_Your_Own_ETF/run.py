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


####################################################################
#
# Description:
#  TODO: Update method description
#
####################################################################
def run():
    exchange = "NYSE"
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

    df = load_market(exchange, analysis_params)

    risk_dist = [0.6, 0.25, 0.15, 0, 0]
    budget = 1000000

    print(
        "---------------------------------------------------------------------------------------------"
    )
    # # objective: call score() with grab ticker data as input and params as input
    print(score(user_defined_params, df, risk_dist, budget))


# Executes Build Your Own ETF
run()
