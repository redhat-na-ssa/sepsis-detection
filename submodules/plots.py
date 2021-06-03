import seaborn as sns

def plotGender(data):
    gender = data
    gender[gender==0] = "female"
    gender[gender==1] = "male"

    sns.countplot(x=gender, dodge=False)

def plotUnit(data):
    Unit1 = data["Unit1"][data["Unit1"] == 1].count()  # patients in Unit1
    Unit2 = data["Unit2"][data["Unit2"] == 1].count()  # patients in Unit2
    totalNa = len(data["Unit1"][(data["Unit1"].isna()) & (data["Unit2"].isna())])

    sns.barplot(x=["Medical ICU", "Surgical ICU", "Not Given"], y=[Unit1, Unit2, totalNa])