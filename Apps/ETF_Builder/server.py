from flask import Flask, request, render_template
import bson
import json
from bson.objectid import ObjectId
from bson.json_util import dumps

from pymongo import MongoClient

import numpy as np
import pandas as pd

from etf_builder import *


import pprint
import sys

sys.path.append("../../Utils")
from Scrub_Fundamental_Stock_Data_By_Defined_Parameters import (
    scrub_fundamental_stock_data_by_defined_parameters,
)

#Flask App Create and Config
app = Flask(__name__)

#MongoDB Connection and Config - possibly move to separate file later



#REPLACE THIS WITH MONGO URL STRING---------------------------------------------------------------
MONGO_URL = None;  #Input the mongoURL



client = MongoClient(MONGO_URL)

db = client.finance_db  #Creating/accessing etf_db

etf_collection = db.etf_collection #Creating/accessing etf_collection






def func_run(params):
    keys_include = ["longName","marketCap","trailingPE","trailingAnnualDividendYield","price","ytdReturn"]
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
    df = pd.read_csv(
        "../../Databases/Fundamental_Stock_Data_NASDAQ/testing_fundamental_stock_data_NASDAQ.csv"
    )
    df = scrub_fundamental_stock_data_by_defined_parameters.execute(df, analysis_params)
    keys = df.keys()
    for key, values in df.items():
        if key not in keys_include:
            df.pop(key)
    riskdist = [.6,.25,.15,0,0]
    budget = 1000000
    # objective: call score() with grab ticker data as input and params as input
    # print(score(params,df,riskdist,budget))
    return(score(params,df,riskdist,budget))


#Main basic route that just displays help info on GET request
@app.route("/", methods=['GET'])
def home():
    if request.method == 'GET':
        output = {
                            "status": "200",
                            "current-endpoint": " GET /",
                            "related-endpoints":    {
                                                    "[POST] /etf-gen":"Generate ETF from input parameters"
                                                    },
        
                }
        

        out_json = json.dumps(output, indent=4, sort_keys=True)

        return(out_json)



@app.route("/etf-gen", methods=['GET','POST'])
def etfgen():
    if request.method == 'GET':

        output =    {
                        "status": "200",
                        "current-endpoint": " GET /",
                        "POST /etf-gen input schema":   {
                                                            "marketCap": [1000000000,4],
                                                            "trailingAnnualDividendYield": [1,3],
                                                            "trailingPE": [30,3]
                                                        }
                    }

        out_json = json.dumps(output, indent=4, sort_keys=True)

        return(out_json)
        


    if request.method == 'POST':

        data = request.get_json()   #JSON of the input

        # data input schema:
        # {
        #     "marketCap":[1000000000,4],
        #     "trailingAnnualDividendYield":[1,3],
        #     "trailingPE":[30,3]
        # }

        func_out = func_run(data)   #DataFrame
        func_out_head = func_out.head()
        print(func_out_head)
        # func_out_head.index = func_out_head.index.map(str)
        # dict_func_out_head = func_out_head.to_dict(orient='index')


        func_out_desc = func_out.describe(include=[np.number])
        dict_func_out_desc = func_out_desc.to_dict(orient='index')
        
        # out_dict =  {
        #                 "etf-build": dict_func_out_head,
        #                 "about": dict_func_out_desc
        #             }

        # #Log minimal Output and get unique ID (_id)
        # mongodoc_id = etf_collection.insert_one(out_dict).inserted_id

        # out_dict_augment =  {
        #                         "etf-build": dict_func_out_head,
        #                         "about": dict_func_out_desc,
        #                         "_id": str(mongodoc_id)
        #                     }

        out_json = json.dumps(dict_func_out_desc, indent=4, sort_keys=True)

        return(out_json)



#Search by id and get metrics
@app.route("/etf-gen/find", methods=['GET'])
def etffind():
    if request.method == 'GET':

        data = request.get_json()

        # data schema: 
        #     {
        #         "_id": "642c75dcc7a4d09a93704e5d"
        #     }

        etf = etf_collection.find_one({"_id": ObjectId(data["_id"])})

        return(dumps(etf, indent=4, sort_keys=True))

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
