import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Read dataset
data = pd.read_csv("play_tennis.csv")

# Create a copy to avoid SettingWithCopyWarning
X = data.iloc[:, :-1].copy()
y = data.iloc[:, -1]

encoders = {}

# Encode categorical features
for column in X.columns:
    le = LabelEncoder()
    X[column] = le.fit_transform(X[column])
    encoders[column] = le

# Encode target
target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y)

# Train ID3 Decision Tree
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

# New sample
sample = pd.DataFrame({
    "Outlook": ["Sunny"],
    "Temperature": ["Cool"],
    "Humidity": ["High"],
    "Wind": ["Weak"]
})

# Encode sample
for column in sample.columns:
    sample[column] = encoders[column].transform(sample[column])

# Predict
prediction = model.predict(sample)

print("Prediction:", target_encoder.inverse_transform(prediction)[0])
