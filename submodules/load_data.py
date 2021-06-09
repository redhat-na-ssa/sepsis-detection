import pandas as pd
import os

DATASET_PATH = os.path.join("datasets", "sepsis")

def load_data(path=DATASET_PATH):
    csv_path = os.path.join(path, "dataSepsis.csv")
    return pd.read_csv(csv_path, sep=";")