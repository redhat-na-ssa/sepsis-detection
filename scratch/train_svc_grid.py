# USAGE
# python train_svc_grid.py
# time python train_svc_grid.py

# import necessary packages
from submodules import config
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
import pandas as pd
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import GridSearchCV

# performance
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score

# load the dataset, separate features and labels, perform split
print("[INFO] loading data...")
dataset = pd.read_csv(config.CSV_PATH, sep=";")
# drop demographic data; with R^2 score = 95%; without R^2 score = 93%
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

# GRID SEARCH CROSS VALIDATION
# initialize the model and 3x parameters
model = SVC()
# the most important part of the svm
kernel = ["linear", "poly", "rbf", "sigmoid", "precomputed"]
# the tolerance for stopping criterion
tolerance = [1e-3, 1e-4, 1e-5, 1e-6]
# strictness, larger the C that harder the classifier (creates overfitting)
C = [1, 1.5, 2, 2.5, 3]
grid = dict(kernel=kernel, tol=tolerance, C=C)

# initialize cross-validation fold and perform a grid search to tune hyperparameters
print("[INFO] grid searching over the hyperparameters...")
# 10 splits repeat 3 times
cvFold = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
# the model with the parameter grid, using all processors/cores to run in parallel to speed up
# smaller mse the better the predictions
gridSearch = GridSearchCV(estimator=model, param_grid=grid, n_jobs=-1,
                          cv=cvFold, scoring="neg_mean_squared_error")
searchResults = gridSearch.fit(X_train, y_train)

# extract the best model and evaluate it
print("[INFO] evaluating...")
bestModel = searchResults.best_estimator_
print("R2: {:2f}".format(bestModel.score(X_test, y_test)))
# train the model *no* hyperparameter tuning
print("[INFO] training with SVC...")
model.fit(X_train, y_train)

# evaluate the model using the R^2 score
print("[INFO] evaluating...")
print("[R2: {:.2f}".format(model.score(X_test, y_test)))