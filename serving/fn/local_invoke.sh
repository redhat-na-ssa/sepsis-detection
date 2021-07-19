curl -X POST -H "Content-Type: application/json" --data '{"HR":103,"O2Sat":90,"Temp":null,"SBP":null,"MAP":null,"DBP":null,"Resp":30,"EtCO2":null,"BaseExcess":21,"HCO3":45,"FiO2":null,"pH":7.37,"PaCO2":90,"SaO2":91,"AST":16,"BUN":14,"Alkalinephos":98,"Calcium":9.3,"Chloride":85,"Creatinine":0.7,"Glucose":193,"Lactate":null,"Magnesium":2,"Phosphate":3.3,"Potassium":3.8,"Bilirubin_total":0.3,"Hct":37.2,"Hgb":12.5,"PTT":null,"WBC":5.7,"Fibrinogen":null,"Platelets":317}' http://127.0.0.1:8080

curl -X POST -H "Content-Type: application/json" --data '{"HR":72.0,"O2Sat":96.0,"Temp":null,"SBP":103.0,"MAP":62.0,"DBP":45.0,"Resp":20.0,"EtCO2":null,"BaseExcess":-1.0,"HCO3":null,"FiO2":null,"pH":7.4,"PaCO2":36.0,"SaO2":98.0,"AST":null,"BUN":null,"Alkalinephos":null,"Calcium":null,"Chloride":null,"Creatinine":null,"Glucose":null,"Lactate":null,"Magnesium":null,"Phosphate":null,"Potassium":null,"Bilirubin_total":null,"Hct":null,"Hgb":null,"PTT":null,"WBC":null,"Fibrinogen":null,"Platelets":null}' http://127.0.0.1:8080

curl -X POST -H "Content-Type: application/json" --data '{"HR":72.0,"O2Sat":96.0,"Temp":null,"SBP":103.0,"MAP":62.0,"DBP":45.0,"Resp":20.0,"EtCO2":null,"BaseExcess":-1.0,"HCO3":null,"FiO2":null,"pH":7.4,"PaCO2":36.0,"SaO2":98.0}' http://127.0.0.1:8080

curl -X POST -H "Content-Type: application/json" --data '{"HR":103,"O2Sat":90,"Temp":null,"Resp":30,"BaseExcess":21,"HCO3":45,"pH":7.37,"PaCO2":90,"SaO2":91,"AST":16,"BUN":14,"Alkalinephos":98,"Calcium":9.3,"Chloride":85,"Creatinine":0.7,"Glucose":193,"Magnesium":2,"Phosphate":3.3,"Potassium":3.8,"Bilirubin_total":0.3,"Hct":37.2,"Hgb":12.5,"WBC":5.7, "Platelets":317}' http://127.0.0.1:8080