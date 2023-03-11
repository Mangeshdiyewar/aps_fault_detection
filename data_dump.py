import pymongo
import pandas as pd
import json

from sensor.config import mongo_client

# Provide the mongodb localhost url to connect python to mongodb.


DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"


if __name__ =="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns:{df.shape}")

    #convert dataframe to jason so it can dumped to mongodb

    df.reset_index(drop=True,inplace=True)

    json_records =list(json.loads(df.T.to_json()).values())
    print(json_records[0])
    
    #insert converted json record to mongodb
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)