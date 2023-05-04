import pandas as pd
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import bson
from IPython.display import display
fileObject = open("mongourl.txt", "r")
uri = fileObject.read()
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection

db = client.finance_db  #Creating/accessing etf_db

etf_collection = db.etf_collection







# test portfoliio upload
profile_dict_test =    {
                        "Name": "Tom's portfolio",
                        "Portfolio":   {
                                        "stock1": {
                                                    "symbol":"MSFT",
                                                    "cap":1000000000,
                                                    "div":1.5,
                                                    "pe":15,
                                                    "shares":5
                                                        },
                                        "stock2": {
                                                    "symbol":"CGNX",
                                                    "cap":20000,
                                                    "div":.8,
                                                    "pe":15,
                                                    "shares":30
                                                        },
                                        "stock3": {
                                                    "symbol":"AAPL",
                                                    "cap":1000000000,
                                                    "div":1,
                                                    "pe":15,
                                                    "shares":5
                                                        }
                                        }
                    }
#tell server todo this
entry = etf_collection.insert_one(profile_dict_test)
#
text_file = open("profile_id.txt", "w")
n = text_file.write(str(entry.inserted_id))
text_file.close()

# signed in =>> profile id
fileObject = open("profile_id.txt", "r")
data = fileObject.read()
id = bson.ObjectId(data)
find_id = etf_collection.find_one({"username":'tomm'})
display(find_id['password'])
# df = pd.DataFrame.from_dict(find_id["Portfolio"])
# df = df.transpose()
# display(df)
# api call > flask


#server




#client