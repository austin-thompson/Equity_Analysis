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
from IPython.display import display


####################################################################
# Description:
#  TODO: Update method description
####################################################################
def scrub_fundamental_stock_data_by_defined_parameters(df, analysis_params):
    # define params for analysis, scrubs data accordingly (ie. drops unnecessary columns)
    df = df.loc[:, analysis_params]

    #### ** DEBUG **
    # display(df)

    # return a dataframe
    return df


####################################################################
# Description:
#  TODO: Update method description
####################################################################
def execute(df, analysis_params):
    return scrub_fundamental_stock_data_by_defined_parameters(df, analysis_params)
