import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("disease_diagnosis.csv")
data.columns = data.columns.str.strip()

X = data.iloc[:, :-1].copy()
y = data.iloc[:, -1]

encoders = {}
for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    encoders[col] = le

target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y.astype(str))

model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

sample = pd.DataFrame({
    "Fever": ["Yes"],
    "Cough": ["Yes"],
    "Headache": ["No"],
    "BodyPain": ["Yes"]
})

sample.columns = sample.columns.str.strip()

for col in sample.columns:
    sample[col] = encoders[col].transform(sample[col].astype(str))

prediction = model.predict(sample)

print("Prediction:",
      target_encoder.inverse_transform(prediction)[0])
