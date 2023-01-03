import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

data_path = "/config/workspace/aps_failure_training_set1.csv"
database_name = 'air_pressure_system'
collection_name = 'sensor_data'

if __name__ == "__main__":
    df = pd.read_csv(data_path)
    print("Rows x Columns = {}".format(df.shape))
    df.reset_index(drop = True, inplace=True)
    json_data = list(json.loads(df.T.to_json()).values())

    #print(json_data[0])git
    client[database_name][collection_name].insert_many(json_data)