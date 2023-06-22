from pymongo import MongoClient
import pandas as pd  
from json import loads
import os

data_frame = pd.read_csv(r"G:\100-days-of-dl\Krish_Naik\FSDS_Ineuron_Course\projects\Heart-Stroke-Prediction-ML-Pipeline\notebooks\data\healthcare-dataset-stroke-data.csv")

records = list(loads(data_frame.T.to_json()).values())

client = MongoClient("mongodb+srv://harshal:harshal@cluster0.ppzqzhg.mongodb.net/?retryWrites=true&w=majority")

database_name = client["iNeuron"]

collection = database_name["heart_stroke"]

collection.insert_many(records)

for i in collection.find():
    print(i)