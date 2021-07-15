# contains a main() function
# USAGE
# python serving/fn/func.py -i data/in/new_data.csv -o data/out/predictions.csv

# OPTIONAL ARGUMENTS
# python serving/fn/func.py -i data/in/new_data.csv -o data/out/predictions.csv -p data/transform/pipeline_minmax.pkl -m models/final/mlp_model.pkl

import pandas as pd
import joblib
import argparse

import json
import csv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input",  type=str, required=True, default="data/in/new_data.csv", help="where to grab data to predict against")
ap.add_argument("-o", "--output", type=str, required=True, default="data/out/predictions.csv", help="where to save the predictions")
ap.add_argument("-p", "--pipeline", type=str, default="data/transform/pipeline.pkl", help="which pipeline to pass the data through")
ap.add_argument("-m", "--model", type=str, default="models/final/xgbc_model.pkl", help="which final model to inference/predict with")
args = vars(ap.parse_args())

INPUT = args["input"]
OUTPUT = args["output"]
PIPELINE = joblib.load(args["pipeline"])
MODEL = joblib.load(args["model"])

def main():
    print("[INFO] loading new patient data...")
    # raw = pd.read_csv(INPUT, sep=",")
    # print("printing raw")
    # print (raw)
     
    # raw.to_json("data/in/new.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
    # raw = pd.read_json("data/in/new.json")
    raw = pd.read_json("data/in/new_single.json")
    print("data frame")
    print(raw)
    
    print("[INFO] dropping non-bio markers...")

    dropped = raw.drop(
        ["Age", "Unit1", "Unit2", "HospAdmTime", "ICULOS", "Gender", "Bilirubin_direct", "TroponinI", "isSepsis"],
        axis=1)
    print("[INFO] passing data through pipeline...")
    print(dropped)
    transformed = PIPELINE.transform(dropped)
    print("[INFO] performing inference...")
    prediction = MODEL.predict(transformed)
    print("[INFO] saving predictions...")
    results = pd.DataFrame(prediction)
    results.columns = ["isspesis"]
    results.to_csv(OUTPUT)

# program
main()