# Systemic Inflammatory Response Syndrome Early Detection

## Project Overview

Goal: An online containerized machine learning microservice to predict patients likely
to become septic based on vital signs and laboratory values powered by 
the Red Hat Portfolio.

# Machine Learning Checklist

## Frame the problem
1. Define the objective: 
   1. early prediction of Sepsis based on patient Vital Signs and Laboratory Values
1. How will the solution be used: 
   1. 
1. What are the current solutions/workarounds: 
   1. provider manually enters values in a Sepsis application
1. How should you frame this problem: 
   1. supervised, online, classification
1. How should performance be measured: 
    1. f1_score - measure provides a way to combine both precision and recall into a single measure that captures both properties
    1. recall - calculated as the number of true positives divided by the total number of true positives and false negatives; good for unbalanced data
    1. precision - quantifies the number of correct positive predictions made; good for unbalanced data
1. What is the minimum performance needed to attain the objective for a prototype: 
   1. 60%
1. What are the comparable problems? can you resuse experience or tools? 
   1. Severe Septic Shock, Refractory Septic Shock, Hypertension, etc.
1. Is human expertise available? 
   1. yes
1. How would you solve the problem manually? 
   1. heuristics
1. List the assumptions made so far:
    1. the data is synthetic used to train the model
1. Verify the assumptions: 
    1. from the data "ICULOS" is the strongest indicator predicting Sepsis, but when removed from the data negatively impacts the models accuracy.
  
## Get the data
> python functions

1. List the data needed and how much:
    1. vital signs
    1. laboratory values
    1. minimum >50k records
1. Where to get the data: 
   1. [Kaggle](https://www.kaggle.com/maxskoryk/datasepsis)
1. How much space will it take: 
   1. 11.4MB
1. Check legal obligations: 
    1. [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
    1. Free to: 
       1. Share — copy and redistribute the material in any medium or format 
       1. Adapt — remix, transform, and build upon the material for any purpose, even commercially.
1. Get access authorizations.
1. Create workspace with enough storage: 
   1. Open Data Hub on Red Hat OpenShift
1. Get the data:
   1. submodules/fetch_data.py
1. Convert the data to a format to manipulate without changing the data: 
   1. submodules/load_data.py
1. Ensure sensitive data is deleted or protected (e.g. anonymized).
1. Check the size and type of data (time series, sample, geographical):
   1. Total size = 11.4MB
   1. Total patient entries = 36,302
   1. Total attributes = 41 
   1. Combined data in .CSV format containing Vitals, Labs and Demographics 
   1. Labeled data column 41 "isSepsis" with 0=False 1=True
   1. Numeric (float64 and int64)
   1. Includes null/NaN

## Explore the data to gain insights
> data-engineering.ipynb

1. Create a copy of the data for exploration
1. Create a Jupyter Notebook to keep record of exploration
1. Study each attribute:
    1. name
    1. data type (numeric, categorical, bounded/un, text, structured, etc.)
    1. % missing values
    1. Noisiness (stochastic, outliers, rounding errors, etc.)
    1. Usefulness for the task
    1. Type of distribution (Gaussian, uniform, logarithmic, etc.)
1. For supervised learning tasks, identify the target attributes.
1. Visualize the data.
1. Study the correlations between attributes.
1. Study how to manually solve the problem. 
1. Identify promising transformations. 
1. Identify extra data that would be useful. (go back to Get the Data.)
1. Document.

## Prepare the data to expose the underlying data patterns for Machine Learning
> data-scientists.ipynb
1. Work on copies of the data.
   1. see data/ subdirectory
1. Write functions for all data transformations.
1. Data cleaning:
    1. fix or remove outliers
    1. fill in missing values
    1. drop rows or columns
1. Feature selection:
    1. drop attributes that provide no useful information for the task
1. Feature engineering:
    1. Discretize continuous features
    1. Decompose features
    1. Add transformations
    1. Aggregate features

## Explore different models and shortlist the best ones
> data-scientists.ipynb
1. Sample smaller training sets (if afforable)
1. Train many models from different categories 
    1. Linear Support Vector Machine "SVM" Support Vector Classifier "SVC"
    1. Naive Bayes
    1. K-Neighbors Classifier 
    1. Random Forest Classifier 
    1. Logistic Regression
    1. Stochastic Gradient Descent "SGD" Classifier
    1. Neural Network Multi-Layer Perceptron Classifier 
    1. XGBoost Classifier
1. Measure and compare performance
    1. Cross Validations with f1_scoring
1. Analyze the most significant variables for each algorithm
1. Analyse the types of errors the models make 
    1. would a human have avoided them?
1. Perform a round of feature engineering and selection
1. Perform 1-2 quick iterations
1. Shortlist the top 3-5 most promising models that make different errors

## Fine-tune the models and select or combine the best solution
> *_model.ipynb

1. Want as much data as possible
1. Fine-tune hyperparameters using cross-validation
1. Try Ensemble methods combining models
1. Measure final model on Test set to estimate the error

## Present the solution
1. Document what you have done
1. Create a presentation
1. Explain why the solution achieves the business objective
1. Highlight interesting points
    1. what worked?
    1. what didn't?
    1. assumptions
    1. limitations

## Launch, monitor and maintain the system
1. Get model ready for production
1. Write monitoring code to check at regular intervals and trigger alerts when it drops
1. Beware: 
    1. slow degradation as data evolves
    1. monitor input quality as well as output
1. Retrain models on fresh data regularly (automate it!)

# Dataset

## Datapoints

Vital signs (columns 1-8)
1. **HR - Heart rate (beats per minute)**
1. **Temp - Temperature (Deg C)**
1. **SBP - Systolic BP (mm Hg)**
1. DBP - Diastolic BP (mm Hg)
1. **MAP - Mean arterial pressure (mm Hg)**
1. **Resp - Respiration rate (breaths per minute)**
1. O2Sat - Pulse oximetry (%)
1. EtCO2 - End tidal carbon dioxide (mm Hg)

Laboratory values (columns 9-34)
1. BaseExcess - Measure of excess bicarbonate (mmol/L)
1. HCO3 - Bicarbonate (mmol/L)
1. FiO2 - Fraction of inspired oxygen (%)
1. pH - N/A
1. PaCO2 - Partial pressure of carbon dioxide from arterial blood (mm Hg)
1. SaO2 - Oxygen saturation from arterial blood (%)
1. AST - Aspartate transaminase (IU/L)
1. BUN - Blood urea nitrogen (mg/dL)
1. Alkalinephos - Alkaline phosphatase (IU/L)
1. Calcium - (mg/dL)
1. Chloride - (mmol/L)
1. Creatinine - (mg/dL)
1. Bilirubin_direct - Bilirubin direct (mg/dL)
1. Glucose - Serum glucose (mg/dL)
1. Lactate - Lactic acid (mg/dL)
1. Magnesium - (mmol/dL)
1. Phosphate - (mg/dL)
1. Potassium - (mmol/L)
1. Bilirubintotal - Total bilirubin (mg/dL)
1. TroponinI - Troponin I (ng/mL)
1. Hct - Hematocrit (%)
1. Hgb - Hemoglobin (g/dL)
1. PTT - partial thromboplastin time (seconds)
1. **WBC - Leukocyte count (count10^3/µL)**
1. Fibrinogen - (mg/dL)
1. **Platelets - (count10^3/µL)**

Demographics (columns 35-40)
1. Age - Years (100 for patients 90 or above)
1. Gender - Female (0) or Male (1)
1. Unit1 - Administrative identifier for ICU unit (MICU)
1. Unit2 - Administrative identifier for ICU unit (SICU)
1. HospAdmTime - Hours between hospital admit and ICU admit
1. ICULOS - ICU length-of-stay (hours since ICU admit)

Outcome (column 41)
1. SepsisLabel - For sepsis patients, SepsisLabel is 1

## Definition of Diseases
In accordance with "Early Recognition and Management of Sepsis in Adults: The First Six Hours"

![image](images/SIRSvsqSOFA.jpg)
### Systemic inflammatory response syndrome (SIRS)
- 2 or more are met:
    - Body temperature > 38.5°C or < 35.0°C
    - Heart rate > 90 beats per minute
    - Respiratory rate > 20 breaths per minute or arterial CO2 tension < 32 mm Hg or need for mechanical ventilation
    - White blood cell count > 12,000/mm3 or < 4,000/mm3 or immature forms > 10%
    
### Sepsis
- Systemic inflammatory response syndrome and documented infection
### Severe sepsis
- Sepsis and at least one sign of organ hypoperfusion or organ dysfunction:
    - Areas of mottled skin 
    - Capillary refilling time ≥ 3 s 
    - Urinary output < 0.5 mL/kg for at least 1 h or renal replacement therapy 
    - Lactates > 2 mmol/L 
    - Abrupt change in mental status or abnormal electroencephalogram 
    - Platelet counts < 100,000/mL or disseminated intravascular coagulation 
    - Acute lung injury—acute respiratory distress syndrome 
    - Cardiac dysfunction (echocardiography)
### Septic shock
- Severe sepsis and one of:
    - Systemic mean blood pressure of < 60 mm Hg (< 80 mm Hg if previous hypertension) after 20–30 mL/kg starch or 40–60 mL/kg serum saline, or pulmonary capillary wedge pressure between 12 and 20 mm Hg
    - Need for dopamine > 5 μg/kg per min or norepinephrine or epinephrine < 0.25 μg/kg per min to maintain mean blood pressure above 60 mm Hg (> 80 mm Hg if previous hypertension)
### Refractory septic shock
- Need for dopamine > 15 μg/kg per min or norepinephrine or epinephrine > 0.25 μg/kg per min to maintain mean blood pressure above 60 mm Hg (> 80 mm Hg if previous hypertension)

Patient with suspicious infection
> Definitions for SIRS and qSOFA. SIRS: systemic inflammatory response syndrome; qSOFA: Sequential Organ Failure Assessment; WBC: white blood cell.

# References
1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6304323/ 
1. https://www.aafp.org/afp/2013/0701/p44.html   
1. https://www.kaggle.com/maxskoryk/datasepsis
1. https://www.nursingcenter.com/ncblog/march-2017/elevated-lactate-%E2%80%93-not-just-a-marker-for-sepsis-an
1. https://unitslab.com/node/74
