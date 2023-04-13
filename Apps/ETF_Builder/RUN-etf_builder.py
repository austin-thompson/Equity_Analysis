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
import matplotlib.pyplot as plt
from etf_builder import *
from IPython.display import display

####################################################################
# Local Imports (clean up this implementation, create pip modules?)
####################################################################
import sys

sys.path.append("../../Utils")
from Scrub_Fundamental_Stock_Data_By_Defined_Parameters import (
    scrub_fundamental_stock_data_by_defined_parameters,
)


####################################################################
# Description:
#  TODO: Update method description
####################################################################
def execute():
    df = pd.read_csv(
        "../../Databases/Fundamental_Stock_Data_NASDAQ/testing_fundamental_stock_data_NASDAQ.csv"
    )

    analysis_params = [
        "quoteType",
        "tickerSymbol",
        "longName",
        "marketCap",
        "trailingPE",
        "trailingAnnualDividendYield",
        "price",
    ]

    df = scrub_fundamental_stock_data_by_defined_parameters.execute(df, analysis_params)

    user_defined_params = {
        "marketCap": [1000000000, 4],
        "trailingAnnualDividendYield": [1, 3],
        "trailingPE": [30, 3],
    }

    user_defined_risk_dist = [0.6, 0.25, 0.15, 0, 0]
    user_defined_budget = 1000000

    print(
        "---------------------------------------------------------------------------------------------"
    )

    print("user_defined_params: " + str(user_defined_params))
    print("user_defined_budget: " + str(user_defined_budget))

    print(
        "---------------------------------------------------------------------------------------------"
    )

    #### ** DEBUG **
    # display(df)

    etf_result = score(
        user_defined_params, df, user_defined_risk_dist, user_defined_budget
    )
    print(etf_result)


# calls execute() to run ETF_Builder
execute()
