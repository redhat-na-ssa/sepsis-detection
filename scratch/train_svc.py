# USAGE
# python train_svc.py
# time python train_svc.py

# import necessary packages
from submodules import config
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score

# load the dataset, separate features and labels, perform split
print("[INFO] loading data...")
dataset = pd.read_csv(config.CSV_PATH, sep=";")
# drop demographic dat
dataset = dataset.drop(["Age",
                        "Unit1",
                        "Unit2",
                        "HospAdmTime",
                        "ICULOS",
                        "Gender"
                        ], axis=1)
# everything but the final label column
dataX = dataset[dataset.columns[:-1]]
# just the label column to predict
dataY = dataset[dataset.columns[-1]]
# 85% training 15% for validation
(X_train, X_test, y_train, y_test) = train_test_split(dataX,
                    dataY, random_state=3, test_size=0.15)

# standardize the the feature values by computing the mean,
# subtracting the mean from the datapoints, then divid by std. deviation
num_pipeline = Pipeline([
                        ('imputer', SimpleImputer(strategy='median')),
                        ('std_scaler', StandardScaler()),
                        ])
# computing mean and std dev, perform the calc on the dataset
X_train = num_pipeline.fit_transform(X_train)
# keep testing separate from training data, never fit_transform on test
X_test = num_pipeline.transform(X_test)

# train the model *no* hyperparameter tuning
print("[INFO] training with SVC...")
model = SVC()
model.fit(X_train, y_train)

# test the model
print("[INFO] predicting...")
svc_predict = model.predict(X_test)

# check the accuracy
print("[INFO] evaluating accuracy...")
print(model.score(X_test, y_test))

# check the f1 score
print("[INFO] recall score...")
print(recall_score(y_test, svc_predict))

# check the f1 score
print("[INFO] f1_score...")
print(f1_score(y_test, svc_predict))

