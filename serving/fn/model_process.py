import pandas as pd
import logging
import joblib

biomarkers = None
pipeline = None
model = None
class ModelProcessor() :

    def load(self, pipelinePath, modelPath) :
        #load model from storage
        global pipeline
        global model

        if pipeline == None:
          logging.warning(f'**************  loading pipeline')
          pipeline = joblib.load(pipelinePath)

        if model == None:
           logging.warning(f'**************  loading model')
           model = joblib.load(modelPath)

        return pipeline, model

    def createDataFrame(self, jsondata) :
        global biomarkers
        # Need to do this otherwise pipeline will throw error
        # "ValueError: X has 24 features, but SimpleImputer is expecting 32 features as input."
        if biomarkers == None:
            #biomarkers = ["HR","O2Sat","Temp","SBP","MAP","DBP","Resp","EtCO2","BaseExcess","HCO3","FiO2","pH","PaCO2","SaO2","AST","BUN","Alkalinephos","Calcium","Chloride","Creatinine","Bilirubin_direct","Glucose","Lactate","Magnesium","Phosphate","Potassium","Bilirubin_total","TroponinI","Hct","Hgb","PTT","WBC","Fibrinogen","Platelets","Age","Gender","Unit1","Unit2","HospAdmTime","ICULOS","isSepsis"]
            #biomarkers = ["Age", "Unit1", "Unit2", "HospAdmTime", "ICULOS", "Gender", "Bilirubin_direct", "TroponinI", "isSepsis"]
            biomarkers = ["HR","O2Sat","Temp","SBP","MAP","DBP","Resp","EtCO2","BaseExcess","HCO3","FiO2","pH","PaCO2","SaO2","AST","BUN","Alkalinephos","Calcium","Chloride","Creatinine","Glucose","Lactate","Magnesium","Phosphate","Potassium","Bilirubin_total","Hct","Hgb","PTT","WBC","Fibrinogen","Platelets"]
        logging.warning(f'**************  checking for missing biomarkers')
        raw = pd.DataFrame(jsondata)  
        for marker in biomarkers:
           if marker not in raw.columns:
             raw[marker] = "NaN"

        return raw

    def transformAndPredict(self, raw, pipeline, model, dropNonBioMarkers = True) :
        print ("predict")
        # dropping non-bio markers
        if dropNonBioMarkers :
            logging.warning(f'**************  "[INFO] dropping non-biomarkers')
            dropped = raw.drop(
            ["Age", "Unit1", "Unit2", "HospAdmTime", "ICULOS", "Gender", "Bilirubin_direct", "TroponinI", "isSepsis"],
              axis=1)
        else :
            dropped = raw

        logging.warning(f'**************  "[INFO] passing transformed data through pipeline... {dropped}')

        # perform inference and predict
        transformed = pipeline.transform(dropped)
        logging.warning(f'[INFO] performing inference...')
        prediction = model.predict(transformed)
        logging.warning(f'[INFO] saving prediction...')
        results = pd.DataFrame(prediction)
        results.columns = ["issepsis"]

        return results
