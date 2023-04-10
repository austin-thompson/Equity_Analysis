####################################################################
# File Name:
#
# Description:
#
#
####################################################################

####################################################################
# Local Imports (clean up this implementation, create pip modules?)
####################################################################
import sys

sys.path.append("../../Utils")
from Get_Fundamental_Stock_Data_By_Exchange import (
    get_fundamental_stock_data_by_exchange,
)


####################################################################
# Description:
#  TODO: Update method description
####################################################################
def execute():
    get_fundamental_stock_data_by_exchange.execute("NASDAQ")


# calls execute() to pull latest NASDAQ data
execute()
