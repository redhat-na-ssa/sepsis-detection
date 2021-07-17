# contains a main() function
# USAGE
# python serving/fn/read_json_func.py -i data/in/new_data.json -o data/out/predictions.csv

# OPTIONAL ARGUMENTS
# python serving/fn/read_json_func.py -i data/in/new_data.json -o data/out/predictions.csv -p data/transform/pipeline_minmax.pkl -m models/final/mlp_model.pkl

import pandas as pd
import argparse

import json
import csv

from model_process import ModelProcessor

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input",  type=str, required=True, default="data/in/new_data.json", help="where to grab data to predict against")
ap.add_argument("-o", "--output", type=str, required=True, default="data/out/predictions.csv", help="where to save the predictions")
ap.add_argument("-p", "--pipeline", type=str, default="data/transform/pipeline.pkl", help="which pipeline to pass the data through")
ap.add_argument("-m", "--model", type=str, default="models/final/xgbc_model.pkl", help="which final model to inference/predict with")
args = vars(ap.parse_args())

INPUT = args["input"]
OUTPUT = args["output"]

def main():
    print("[INFO] loading new patient data...")
    modelprocessor = ModelProcessor()
    PIPELINE, MODEL = modelprocessor.load(pipelinePath = args["pipeline"], modelPath = args["model"])


    # to convert from csv to json
    # raw = pd.read_csv(INPUT, sep=",")
    # print("printing raw")
    # print (raw)
    #save to json
    # raw.to_json("data/in/new.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
   
    # process json
    raw = pd.read_json(INPUT)
    print("data frame")
    print(raw)

    results = modelprocessor.transformAndPredict(raw, pipeline = PIPELINE, model = MODEL)
    results.to_csv(OUTPUT)

# program
main()