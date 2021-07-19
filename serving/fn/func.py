from parliament import Context
import logging
import json

from model_process import ModelProcessor

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

    # helper to process the model
    modelprocessor = ModelProcessor()

    # get json data from request or cloud event
    # attempt to get data from HTTP Request or cloud event
    if hasattr(context, "cloud_event") and hasattr(context.cloud_event, "data"):
         data = context.cloud_event.data
    elif hasattr(context, "request"):
         data = json.loads(context.request.get_data())
    else : 
         data = context #assume this is from test...
    logging.warning(f'**************  data from request: {data}')

    #convert to index then creating data frame
    jsondata = json.loads("[" + json.dumps(data) + "]") #convert to string first
    raw = modelprocessor.createDataFrame(jsondata)
    logging.warning(f'**************  "[INFO] raw dataframe... {raw}') 

    # # load pipeline and model 
    pipeline, model = modelprocessor.load(pipelinePath = "pipeline.pkl", modelPath = "xgbc_model.pkl") 

    # get results
    results = modelprocessor.transformAndPredict(raw, pipeline, model, dropNonBioMarkers = False )
    # there should only be one
    for index, row in results.iterrows():
        issepsis = row["issepsis"]

    # return results
    body = { "issepsis": int(issepsis) }
    #headers = { "content-type": "application/json" }
    logging.warning(f'**************  "[INFO] prediction... {body}')    
    return { "issepsis": int(issepsis) }, 200 
    #return body, 200 , headers
