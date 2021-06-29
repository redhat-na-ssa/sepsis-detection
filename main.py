# Usage
# python main.py

# Import packages
from submodules.load_data import load_data
import pandas as pd
import joblib

# Load the data
print("[INFO] loading new patient data...")
#data = load_data()
csv_path = "data/in/new_data.csv"
data = pd.read_csv(csv_path, sep=",")

# IMPORTANT: the model was trained on the data shape of the kaggle dataset less the columns
# if you undo or remove more columns, the model needs to be retrained
print("[INFO] dropping non-bio markers...")
X = data.drop(["Age", "Unit1", "Unit2", "HospAdmTime", "ICULOS", "Gender", "Bilirubin_direct", "TroponinI", "isSepsis"], axis=1)
y = data[data.columns[-1]]

# Load and run transformation pipeline
print("[INFO] running data through pipeline...")
pipeline = joblib.load("data/transform/pipeline.pkl")
X_ready = pipeline.transform(X)

# Load and run the model
print("[INFO] run predictions on new patient data...")
model = joblib.load("models/final/xgbc_model.pkl")
isspesis = model.predict(X_ready)

# Save the columns
print("[INFO] saving predictions...")
results = pd.DataFrame(isspesis)
results.columns = ["isspesis"]
results.to_csv("data/out/new_data_results.csv")