import unittest

func = __import__("func")

class TestFunc(unittest.TestCase):

  def test_func(self) :

    #test no sepsis
    data = {
   "HR":103,
   "O2Sat":90,
   "Temp":"NaN",
   "SBP":"NaN",
   "MAP":"NaN",
   "DBP":"NaN",
   "Resp":30,
   "EtCO2":"NaN",
   "BaseExcess":21,
   "HCO3":45,
   "FiO2":"NaN",
   "pH":7.37,
   "PaCO2":90,
   "SaO2":91,
   "AST":16,
   "BUN":14,
   "Alkalinephos":98,
   "Calcium":9.3,
   "Chloride":85,
   "Creatinine":0.7,
   "Bilirubin_direct":"NaN",
   "Glucose":193,
   "Lactate":"NaN",
   "Magnesium":2,
   "Phosphate":3.3,
   "Potassium":3.8,
   "Bilirubin_total":0.3,
   "TroponinI":"NaN",
   "Hct":37.2,
   "Hgb":12.5,
   "PTT":"NaN",
   "WBC":5.7,
   "Fibrinogen":"NaN",
   "Platelets":317,
   "Age":83.14,
   "Gender":0,
   "Unit1":"NaN",
   "Unit2":"NaN",
   "HospAdmTime":"-0.03",
   "ICULOS":17,
   "isSepsis":0
}

   # test yes sepsis
    data2 = {
   "HR":72.0,
   "O2Sat":96.0,
   "Temp":"NaN",
   "SBP":103.0,
   "MAP":62.0,
   "DBP":45.0,
   "Resp":20.0,
   "EtCO2":"NaN",
   "BaseExcess":-1.0,
   "HCO3":"NaN",
   "FiO2":"NaN",
   "pH":7.4,
   "PaCO2":36.0,
   "SaO2":98.0,
   "AST":"NaN",
   "BUN":"NaN",
   "Alkalinephos":"NaN",
   "Calcium":"NaN",
   "Chloride":"NaN",
   "Creatinine":"NaN",
   "Bilirubin_direct":"NaN",
   "Glucose":"NaN",
   "Lactate":"NaN",
   "Magnesium":"NaN",
   "Phosphate":"NaN",
   "Potassium":"NaN",
   "Bilirubin_total":"NaN",
   "TroponinI":"NaN",
   "Hct":"NaN",
   "Hgb":"NaN",
   "PTT":"NaN",
   "WBC":"NaN",
   "Fibrinogen":"NaN",
   "Platelets":"NaN",
   "Age":77.26,
   "Gender":0,
   "Unit1":0.0,
   "Unit2":1.0,
   "HospAdmTime":-135.81,
   "ICULOS":19,
   "isSepsis":1
}
  
    #attempts to create cloud event request
    # attributes = {
    # "type": "com.example.sampletype1",
    # "source": "https://example.com/event-producer",
    # }
    # event = CloudEvent(attributes, data)
    # headers, body = to_structured(event)
    # print(body)
    # print(headers)
  #   assert event is not None
  #  # assert event.EventType() == data.ce_type
  #   assert event.EventID() == data.ce_id
  #   assert event.ContentType() == data.contentTyp
    # print(event)

    # m = marshaller.NewDefaultHTTPMarshaller()
    # http_headers = {"content-type": "application/cloudevents+json"}
    # #event = m.FromRequest(event_class(), headers, body)
    # new_headers, _ = m.ToRequest(body, converters.TypeStructured, lambda x: x)
    # print(new_headers)
    
    #resp, code, headers = func.main(data)
    resp, code = func.main(data)
    self.assertEqual(resp["issepsis"], 0)
    self.assertEqual(code, 200)
    #self.assertEqual(headers["content-type"], "application/json")

    # resp, code, headers = func.main(data2)
    resp, code = func.main(data2)
    self.assertEqual(resp["issepsis"], 1)
    self.assertEqual(code, 200)
    #self.assertEqual(headers["content-type"], "application/json")

    # test with missing fields

    # no sepsis
    data = {
   "HR":103,
   "O2Sat":90,
   "Resp":30,
   "BaseExcess":21,
   "HCO3":45,
   "pH":7.37,
   "PaCO2":90,
   "SaO2":91,
   "AST":16,
   "BUN":14,
   "Alkalinephos":98,
   "Calcium":9.3,
   "Chloride":85,
   "Creatinine":0.7,
   "Glucose":193,
   "Magnesium":2,
   "Phosphate":3.3,
   "Potassium":3.8,
   "Bilirubin_total":0.3,
   "Hct":37.2,
   "Hgb":12.5,
   "WBC":5.7,
   "Platelets":317,
   "Age":83.14,
   "Gender":0,
   "HospAdmTime":"-0.03",
   "ICULOS":17
}

    #sepsis
    data2 = {
   "HR":72.0,
   "O2Sat":96.0,
   "SBP":103.0,
   "MAP":62.0,
   "DBP":45.0,
   "Resp":20.0,
   "BaseExcess":-1.0,
   "pH":7.4,
   "PaCO2":36.0,
   "SaO2":98.0,
   "Age":77.26,
   "Gender":0,
   "Unit1":0.0,
   "Unit2":1.0,
   "HospAdmTime":-135.81,
   "ICULOS":19,
}

    # resp, code = func.main(data)
    # self.assertEqual(resp["issepsis"], 1)
    # self.assertEqual(code, 200)    
    
    # resp, code = func.main(data2)
    # self.assertEqual(resp["issepsis"], 1)
    # self.assertEqual(code, 200)
  
if __name__ == "__main__":
  unittest.main()


#data as index
#     data = [{
#    "HR":103,
#    "O2Sat":90,
#    "Temp":"NaN",
#    "SBP":"NaN",
#    "MAP":"NaN",
#    "DBP":"NaN",
#    "Resp":30,
#    "EtCO2":"NaN",
#    "BaseExcess":21,
#    "HCO3":45,
#    "FiO2":"NaN",
#    "pH":7.37,
#    "PaCO2":90,
#    "SaO2":91,
#    "AST":16,
#    "BUN":14,
#    "Alkalinephos":98,
#    "Calcium":9.3,
#    "Chloride":85,
#    "Creatinine":0.7,
#    "Bilirubin_direct":"NaN",
#    "Glucose":193,
#    "Lactate":"NaN",
#    "Magnesium":2,
#    "Phosphate":3.3,
#    "Potassium":3.8,
#    "Bilirubin_total":0.3,
#    "TroponinI":"NaN",
#    "Hct":37.2,
#    "Hgb":12.5,
#    "PTT":"NaN",
#    "WBC":5.7,
#    "Fibrinogen":"NaN",
#    "Platelets":317,
#    "Age":83.14,
#    "Gender":0,
#    "Unit1":"NaN",
#    "Unit2":"NaN",
#    "HospAdmTime":-0.03,
#    "ICULOS":17,
#    "isSepsis":0
# }]    
# 
# data2 = [
#     {
#    "HR":72.0,
#    "O2Sat":96.0,
#    "Temp":"NaN",
#    "SBP":103.0,
#    "MAP":62.0,
#    "DBP":45.0,
#    "Resp":20.0,
#    "EtCO2":"NaN",
#    "BaseExcess":-1.0,
#    "HCO3":"NaN",
#    "FiO2":"NaN",
#    "pH":7.4,
#    "PaCO2":36.0,
#    "SaO2":98.0,
#    "AST":"NaN",
#    "BUN":"NaN",
#    "Alkalinephos":"NaN",
#    "Calcium":"NaN",
#    "Chloride":"NaN",
#    "Creatinine":"NaN",
#    "Bilirubin_direct":"NaN",
#    "Glucose":"NaN",
#    "Lactate":"NaN",
#    "Magnesium":"NaN",
#    "Phosphate":"NaN",
#    "Potassium":"NaN",
#    "Bilirubin_total":"NaN",
#    "TroponinI":"NaN",
#    "Hct":"NaN",
#    "Hgb":"NaN",
#    "PTT":"NaN",
#    "WBC":"NaN",
#    "Fibrinogen":"NaN",
#    "Platelets":"NaN",
#    "Age":77.26,
#    "Gender":0,
#    "Unit1":0.0,
#    "Unit2":1.0,
#    "HospAdmTime":-135.81,
#    "ICULOS":19,
#    "isSepsis":1
# }]