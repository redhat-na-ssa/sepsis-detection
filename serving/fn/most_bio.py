# contains a main() function
# USAGE
# python serving/fn/determineMostBioData.py -i data/in/new_data.json 

import json
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input",  type=str,  default="data/in/new_json.csv", help="where to grab data to predict against")

args = vars(ap.parse_args())
INPUT = args["input"]

def main():
    print(args)
    print("[INFO] determine the data with the most information ...")

    maxRecordSoFar = None
    maxNonNaNMarkers = 0
    f = open(INPUT,"r")
    jsonData = json.loads(f.read())
  #  print(jsonData)

    #remove non-essential bio-markers
    # biomarkers = ["HR","O2Sat","Temp","SBP","MAP","DBP","Resp","EtCO2","BaseExcess","HCO3","FiO2","pH","PaCO2","SaO2","AST","BUN","Alkalinephos","Calcium","Chloride","Creatinine","Bilirubin_direct","Glucose","Lactate","Magnesium","Phosphate","Potassium","Bilirubin_total","TroponinI","Hct","Hgb","PTT","WBC","Fibrinogen","Platelets","Age","Gender","Unit1","Unit2","HospAdmTime","ICULOS","isSepsis"]
    biomarkers = ["HR","O2Sat","Temp","SBP","MAP","DBP","Resp","EtCO2","BaseExcess","HCO3","FiO2","pH","PaCO2","SaO2","AST","BUN","Alkalinephos","Calcium","Chloride","Creatinine","Glucose","Lactate","Magnesium","Phosphate","Potassium","Bilirubin_total","Hct","Hgb","PTT","WBC","Fibrinogen","Platelets"]

    for record in jsonData:

        # count the number of records
        currentMax = 0
        for marker in biomarkers :
            if record[marker] != None :
                currentMax+=1

        if record["Temp"] != None :
            print("current max")
            print(currentMax)
            print(record)
            
        if currentMax > maxNonNaNMarkers : # add check for non-null Temp
            # print("current max")
            # print(currentMax)
            # print(record)
            maxRecordSoFar = record 
            maxNonNaNMarkers = currentMax 

    print("maxrecord")
    print(maxNonNaNMarkers)
    print(maxRecordSoFar)
        
        


        

# program
main()