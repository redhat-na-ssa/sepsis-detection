
package com.redhat.demo.sepsis.beans;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * Root Type for PatientVitals
 * <p>
 * Vitals information taken from a patient at a particular point in time.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "HR",
    "O2Sat",
    "Temp",
    "SBP",
    "MAP",
    "DBP",
    "Resp",
    "EtCO2",
    "BaseExcess",
    "HCO3",
    "FiO2",
    "pH",
    "PaCO2",
    "SaO2",
    "AST",
    "BUN",
    "Alkalinephos",
    "Calcium",
    "Chloride",
    "Creatinine",
    "Bilirubin_direct",
    "Glucose",
    "Lactate",
    "Magnesium",
    "Phosphate",
    "Potassium",
    "Bilirubin_total",
    "TroponinI",
    "Hct",
    "Hgb",
    "PTT",
    "WBC",
    "Fibrinogen",
    "Platelets",
    "Age",
    "Gender",
    "Unit1",
    "Unit2",
    "HospAdmTime",
    "ICULOS",
    "isSepsis"
})
public class PatientVitals {

    @JsonProperty("HR")
    private String hr;
    @JsonProperty("O2Sat")
    private String o2Sat;
    @JsonProperty("Temp")
    private String temp;
    @JsonProperty("SBP")
    private String sbp;
    @JsonProperty("MAP")
    private String map;
    @JsonProperty("DBP")
    private String dbp;
    @JsonProperty("Resp")
    private String resp;
    @JsonProperty("EtCO2")
    private String etCO2;
    @JsonProperty("BaseExcess")
    private String baseExcess;
    @JsonProperty("HCO3")
    private String hco3;
    @JsonProperty("FiO2")
    private String fiO2;
    @JsonProperty("pH")
    private String pH;
    @JsonProperty("PaCO2")
    private String paCO2;
    @JsonProperty("SaO2")
    private String saO2;
    @JsonProperty("AST")
    private String ast;
    @JsonProperty("BUN")
    private String bun;
    @JsonProperty("Alkalinephos")
    private String alkalinephos;
    @JsonProperty("Calcium")
    private String calcium;
    @JsonProperty("Chloride")
    private String chloride;
    @JsonProperty("Creatinine")
    private String creatinine;
    @JsonProperty("Bilirubin_direct")
    private String bilirubinDirect;
    @JsonProperty("Glucose")
    private String glucose;
    @JsonProperty("Lactate")
    private String lactate;
    @JsonProperty("Magnesium")
    private String magnesium;
    @JsonProperty("Phosphate")
    private String phosphate;
    @JsonProperty("Potassium")
    private String potassium;
    @JsonProperty("Bilirubin_total")
    private String bilirubinTotal;
    @JsonProperty("TroponinI")
    private String troponinI;
    @JsonProperty("Hct")
    private String hct;
    @JsonProperty("Hgb")
    private String hgb;
    @JsonProperty("PTT")
    private String ptt;
    @JsonProperty("WBC")
    private String wbc;
    @JsonProperty("Fibrinogen")
    private String fibrinogen;
    @JsonProperty("Platelets")
    private String platelets;
    @JsonProperty("Age")
    private String age;
    @JsonProperty("Gender")
    private String gender;
    @JsonProperty("Unit1")
    private String unit1;
    @JsonProperty("Unit2")
    private String unit2;
    @JsonProperty("HospAdmTime")
    private String hospAdmTime;
    @JsonProperty("ICULOS")
    private String iculos;
    @JsonProperty("isSepsis")
    private String isSepsis;

    @JsonProperty("HR")
    public String getHr() {
        return hr;
    }

    @JsonProperty("HR")
    public void setHr(String hr) {
        this.hr = hr;
    }

    @JsonProperty("O2Sat")
    public String getO2Sat() {
        return o2Sat;
    }

    @JsonProperty("O2Sat")
    public void setO2Sat(String o2Sat) {
        this.o2Sat = o2Sat;
    }

    @JsonProperty("Temp")
    public String getTemp() {
        return temp;
    }

    @JsonProperty("Temp")
    public void setTemp(String temp) {
        this.temp = temp;
    }

    @JsonProperty("SBP")
    public String getSbp() {
        return sbp;
    }

    @JsonProperty("SBP")
    public void setSbp(String sbp) {
        this.sbp = sbp;
    }

    @JsonProperty("MAP")
    public String getMap() {
        return map;
    }

    @JsonProperty("MAP")
    public void setMap(String map) {
        this.map = map;
    }

    @JsonProperty("DBP")
    public String getDbp() {
        return dbp;
    }

    @JsonProperty("DBP")
    public void setDbp(String dbp) {
        this.dbp = dbp;
    }

    @JsonProperty("Resp")
    public String getResp() {
        return resp;
    }

    @JsonProperty("Resp")
    public void setResp(String resp) {
        this.resp = resp;
    }

    @JsonProperty("EtCO2")
    public String getEtCO2() {
        return etCO2;
    }

    @JsonProperty("EtCO2")
    public void setEtCO2(String etCO2) {
        this.etCO2 = etCO2;
    }

    @JsonProperty("BaseExcess")
    public String getBaseExcess() {
        return baseExcess;
    }

    @JsonProperty("BaseExcess")
    public void setBaseExcess(String baseExcess) {
        this.baseExcess = baseExcess;
    }

    @JsonProperty("HCO3")
    public String getHco3() {
        return hco3;
    }

    @JsonProperty("HCO3")
    public void setHco3(String hco3) {
        this.hco3 = hco3;
    }

    @JsonProperty("FiO2")
    public String getFiO2() {
        return fiO2;
    }

    @JsonProperty("FiO2")
    public void setFiO2(String fiO2) {
        this.fiO2 = fiO2;
    }

    @JsonProperty("pH")
    public String getpH() {
        return pH;
    }

    @JsonProperty("pH")
    public void setpH(String pH) {
        this.pH = pH;
    }

    @JsonProperty("PaCO2")
    public String getPaCO2() {
        return paCO2;
    }

    @JsonProperty("PaCO2")
    public void setPaCO2(String paCO2) {
        this.paCO2 = paCO2;
    }

    @JsonProperty("SaO2")
    public String getSaO2() {
        return saO2;
    }

    @JsonProperty("SaO2")
    public void setSaO2(String saO2) {
        this.saO2 = saO2;
    }

    @JsonProperty("AST")
    public String getAst() {
        return ast;
    }

    @JsonProperty("AST")
    public void setAst(String ast) {
        this.ast = ast;
    }

    @JsonProperty("BUN")
    public String getBun() {
        return bun;
    }

    @JsonProperty("BUN")
    public void setBun(String bun) {
        this.bun = bun;
    }

    @JsonProperty("Alkalinephos")
    public String getAlkalinephos() {
        return alkalinephos;
    }

    @JsonProperty("Alkalinephos")
    public void setAlkalinephos(String alkalinephos) {
        this.alkalinephos = alkalinephos;
    }

    @JsonProperty("Calcium")
    public String getCalcium() {
        return calcium;
    }

    @JsonProperty("Calcium")
    public void setCalcium(String calcium) {
        this.calcium = calcium;
    }

    @JsonProperty("Chloride")
    public String getChloride() {
        return chloride;
    }

    @JsonProperty("Chloride")
    public void setChloride(String chloride) {
        this.chloride = chloride;
    }

    @JsonProperty("Creatinine")
    public String getCreatinine() {
        return creatinine;
    }

    @JsonProperty("Creatinine")
    public void setCreatinine(String creatinine) {
        this.creatinine = creatinine;
    }

    @JsonProperty("Bilirubin_direct")
    public String getBilirubinDirect() {
        return bilirubinDirect;
    }

    @JsonProperty("Bilirubin_direct")
    public void setBilirubinDirect(String bilirubinDirect) {
        this.bilirubinDirect = bilirubinDirect;
    }

    @JsonProperty("Glucose")
    public String getGlucose() {
        return glucose;
    }

    @JsonProperty("Glucose")
    public void setGlucose(String glucose) {
        this.glucose = glucose;
    }

    @JsonProperty("Lactate")
    public String getLactate() {
        return lactate;
    }

    @JsonProperty("Lactate")
    public void setLactate(String lactate) {
        this.lactate = lactate;
    }

    @JsonProperty("Magnesium")
    public String getMagnesium() {
        return magnesium;
    }

    @JsonProperty("Magnesium")
    public void setMagnesium(String magnesium) {
        this.magnesium = magnesium;
    }

    @JsonProperty("Phosphate")
    public String getPhosphate() {
        return phosphate;
    }

    @JsonProperty("Phosphate")
    public void setPhosphate(String phosphate) {
        this.phosphate = phosphate;
    }

    @JsonProperty("Potassium")
    public String getPotassium() {
        return potassium;
    }

    @JsonProperty("Potassium")
    public void setPotassium(String potassium) {
        this.potassium = potassium;
    }

    @JsonProperty("Bilirubin_total")
    public String getBilirubinTotal() {
        return bilirubinTotal;
    }

    @JsonProperty("Bilirubin_total")
    public void setBilirubinTotal(String bilirubinTotal) {
        this.bilirubinTotal = bilirubinTotal;
    }

    @JsonProperty("TroponinI")
    public String getTroponinI() {
        return troponinI;
    }

    @JsonProperty("TroponinI")
    public void setTroponinI(String troponinI) {
        this.troponinI = troponinI;
    }

    @JsonProperty("Hct")
    public String getHct() {
        return hct;
    }

    @JsonProperty("Hct")
    public void setHct(String hct) {
        this.hct = hct;
    }

    @JsonProperty("Hgb")
    public String getHgb() {
        return hgb;
    }

    @JsonProperty("Hgb")
    public void setHgb(String hgb) {
        this.hgb = hgb;
    }

    @JsonProperty("PTT")
    public String getPtt() {
        return ptt;
    }

    @JsonProperty("PTT")
    public void setPtt(String ptt) {
        this.ptt = ptt;
    }

    @JsonProperty("WBC")
    public String getWbc() {
        return wbc;
    }

    @JsonProperty("WBC")
    public void setWbc(String wbc) {
        this.wbc = wbc;
    }

    @JsonProperty("Fibrinogen")
    public String getFibrinogen() {
        return fibrinogen;
    }

    @JsonProperty("Fibrinogen")
    public void setFibrinogen(String fibrinogen) {
        this.fibrinogen = fibrinogen;
    }

    @JsonProperty("Platelets")
    public String getPlatelets() {
        return platelets;
    }

    @JsonProperty("Platelets")
    public void setPlatelets(String platelets) {
        this.platelets = platelets;
    }

    @JsonProperty("Age")
    public String getAge() {
        return age;
    }

    @JsonProperty("Age")
    public void setAge(String age) {
        this.age = age;
    }

    @JsonProperty("Gender")
    public String getGender() {
        return gender;
    }

    @JsonProperty("Gender")
    public void setGender(String gender) {
        this.gender = gender;
    }

    @JsonProperty("Unit1")
    public String getUnit1() {
        return unit1;
    }

    @JsonProperty("Unit1")
    public void setUnit1(String unit1) {
        this.unit1 = unit1;
    }

    @JsonProperty("Unit2")
    public String getUnit2() {
        return unit2;
    }

    @JsonProperty("Unit2")
    public void setUnit2(String unit2) {
        this.unit2 = unit2;
    }

    @JsonProperty("HospAdmTime")
    public String getHospAdmTime() {
        return hospAdmTime;
    }

    @JsonProperty("HospAdmTime")
    public void setHospAdmTime(String hospAdmTime) {
        this.hospAdmTime = hospAdmTime;
    }

    @JsonProperty("ICULOS")
    public String getIculos() {
        return iculos;
    }

    @JsonProperty("ICULOS")
    public void setIculos(String iculos) {
        this.iculos = iculos;
    }

    @JsonProperty("isSepsis")
    public String getIsSepsis() {
        return isSepsis;
    }

    @JsonProperty("isSepsis")
    public void setIsSepsis(String isSepsis) {
        this.isSepsis = isSepsis;
    }

}
