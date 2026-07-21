import pandas as pd

data = pd.read_csv("disease_diagnosis.csv")

attributes = data.iloc[:, :-1].values
target = data["Disease"].values

hypothesis = ['Ø'] * len(attributes[0])

for i in range(len(attributes)):
    if target[i] == "Positive":
        if hypothesis[0] == 'Ø':
            hypothesis = list(attributes[i])
        else:
            for j in range(len(hypothesis)):
                if hypothesis[j] != attributes[i][j]:
                    hypothesis[j] = '?'

print("Final Hypothesis:")
print(hypothesis)
