import unittest

func = __import__("func")

class TestFunc(unittest.TestCase):

  def check_data(self, biomarkers, expectedResult) :
    #resp, code, headers = func.main(biomarkers)
    resp, code = func.main(biomarkers)
    self.assertEqual(resp["issepsis"], expectedResult)
    self.assertEqual(code, 200)
    #self.assertEqual(headers["content-type"], "application/json")
    return biomarkers, expectedResult

  def test_func(self) :

    #test no sepsis
    data = {
   "HR":103,
   "O2Sat":90,
   "Temp": None,
   "SBP": None,
   "MAP": None,
   "DBP": None,
   "Resp":30,
   "EtCO2": None,
   "BaseExcess":21,
   "HCO3":45,
   "FiO2": None,
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
   "Lactate": None,
   "Magnesium":2,
   "Phosphate":3.3,
   "Potassium":3.8,
   "Bilirubin_total":0.3,
   "Hct":37.2,
   "Hgb":12.5,
   "PTT": None,
   "WBC":5.7,
   "Fibrinogen": None,
   "Platelets":317
}

   # test yes sepsis
    data2 = {
   "HR":72.0,
   "O2Sat":96.0,
   "Temp": None,
   "SBP":103.0,
   "MAP":62.0,
   "DBP":45.0,
   "Resp":20.0,
   "EtCO2": None,
   "BaseExcess":-1.0,
   "HCO3": None,
   "FiO2": None,
   "pH":7.4,
   "PaCO2":36.0,
   "SaO2":98.0,
   "AST": None,
   "BUN": None,
   "Alkalinephos": None,
   "Calcium": None,
   "Chloride": None,
   "Creatinine": None,
   "Glucose": None,
   "Lactate": None,
   "Magnesium": None,
   "Phosphate": None,
   "Potassium": None,
   "Bilirubin_total": None,
   "Hct": None,
   "Hgb": None,
   "PTT": None,
   "WBC": None,
   "Fibrinogen": None,
   "Platelets": None
}
  
    #run tests
    self.check_data(biomarkers = data, expectedResult = 0)
    self.check_data(biomarkers = data2, expectedResult = 1)

    # test with missing fields
    # no sepsis ..for some reason if we remove Temp from list the expected result is wrong. TODO: investigate
    data = {
   "HR":103,
   "O2Sat":90,
   "Temp": None,
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
   "Platelets":317
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
   "SaO2":98.0
}

    print("******Checking missing biomarkers*****")
    self.check_data(data, 0)
    self.check_data(data2, 1)

  
if __name__ == "__main__":
  unittest.main()
