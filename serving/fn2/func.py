from parliament import Context
import pandas as pd
import joblib
import logging
import json

pipeline = None
model = None

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
    # logging.warning(f'**************  context.request: {r}')
    # logging.warning(f'**************  content_length: {r.content_length}')
   # logging.warning(f'**************  get_data: {r.get_data()}')
    # logging.warning(f'**************  get_data: {context.cloud_event.data}')
    # logging.warning(f'**************  type: {type(r.get_data())}')
    # logging.warning(f'**************  headers: {r.headers}')

   #load model from storage
    global pipeline
    global model

    # get json data from request or cloud event
    data = context 
    # if context :
  #     print(context)
    if hasattr(context, "request"):
         data = json.loads(context.request.get_data())
    if hasattr(context, "cloud_event"):
         if hasattr(context.cloud_event, "data"):
            data = context.cloud_event.data

    logging.warning(f'**************  data from request: {data}')

    #convert to index before creating data frame
    jsondata = json.loads("[" + json.dumps(data) + "]") #convert to string first
   # print(jsondata)
    raw = pd.DataFrame(jsondata)  
    logging.warning(f'**************  "[INFO] raw dataframe... {raw}') 
   # print(raw)



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
