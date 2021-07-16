from parliament import Context
import pandas as pd
import joblib
import logging
import json

pipeline = None
model = None
biomarkers = None

def main(context: Context):

    """ 
    Function template
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """

    #
    # Debug output.
    #
    logging.warning(f'')
    logging.warning(f'')
    logging.warning(f'**************************************************************')
    logging.warning(f'************** main() called.')

    #load model from storage
    global pipeline
    global model

    # get json data from request or cloud event
    data = context 

    # attempt to get data from HTTP Request or cloud event
    if hasattr(context, "cloud_event") and hasattr(context.cloud_event, "data"):
         data = context.cloud_event.data
    if hasattr(context, "request"):
         data = json.loads(context.request.get_data())


    logging.warning(f'**************  data from request: {data}')

    # add missing biomarkers to the data 
    global biomarkers
    if biomarkers == None:
        biomarkers = ["HR","O2Sat","Temp","SBP","MAP","DBP","Resp","EtCO2","BaseExcess","HCO3","FiO2","pH","PaCO2","SaO2","AST","BUN","Alkalinephos","Calcium","Chloride","Creatinine","Bilirubin_direct","Glucose","Lactate","Magnesium","Phosphate","Potassium","Bilirubin_total","TroponinI","Hct","Hgb","PTT","WBC","Fibrinogen","Platelets","Age","Gender","Unit1","Unit2","HospAdmTime","ICULOS","isSepsis"]
    # print(biomarkers)

    # logging.warning(f'**************  checking for missing biomarkers')
    # OR should we add this to the data frame?
    # for marker in biomarkers:
    #     if marker not in data:
    #         data[marker] = "NaN"

    #convert to index before creating data frame
    jsondata = json.loads("[" + json.dumps(data) + "]") #convert to string first
    #logging.warning(f'**************  "[INFO] updated data with all biomarkers... {jsondata}') 
   
    logging.warning(f'**************  checking for missing biomarkers')
    raw = pd.DataFrame(jsondata)  
    for marker in biomarkers:
        if marker not in raw.columns:
            raw[marker] = "NaN"

    logging.warning(f'**************  "[INFO] raw dataframe... {raw}') 
 
    # load pipeline and model 
    if pipeline == None:
        logging.warning(f'**************  loading pipeline')
        pipeline = joblib.load("pipeline.pkl")

    if model == None:
        logging.warning(f'**************  loading model')
        model = joblib.load("xgbc_model.pkl")

    # dropping non-bio markers
    dropped = raw.drop(
        ["Age", "Unit1", "Unit2", "HospAdmTime", "ICULOS", "Gender", "Bilirubin_direct", "TroponinI", "isSepsis"],
        axis=1)
    logging.warning(f'**************  "[INFO] passing transformed data through pipeline... {dropped}')

    # perform inference and predict
    transformed = pipeline.transform(dropped)
    logging.warning(f'[INFO] performing inference...')
    prediction = model.predict(transformed)
    logging.warning(f'[INFO] saving prediction...')
    results = pd.DataFrame(prediction)
    results.columns = ["issepsis"]
    for index, row in results.iterrows():
        issepsis = row["issepsis"]

    # return results
    body = { "issepsis": int(issepsis) }
    #headers = { "content-type": "application/json" }
    logging.warning(f'**************  "[INFO] prediction... {body}')    
    return { "issepsis": int(issepsis) }, 200 
    #return body, 200 , headers
