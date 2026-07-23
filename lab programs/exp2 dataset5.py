import pandas as pd
import numpy as np

data = pd.read_csv("email_spam.csv")
concepts = np.array(data.iloc[:, :-1])
target = np.array(data.iloc[:, -1])

specific = concepts[0].copy()
general = [["?" for _ in range(len(specific))] for _ in range(len(specific))]

print("Initial Specific Hypothesis:", specific)
print("Initial General Hypothesis:", general)

for i, h in enumerate(concepts):
    if target[i] == "Positive":
        for x in range(len(specific)):
            if h[x] != specific[x]:
                specific[x] = "?"
                general[x][x] = "?"
    else:
        for x in range(len(specific)):
            if h[x] != specific[x]:
                general[x][x] = specific[x]
            else:
                general[x][x] = "?"

print("\nFinal Specific Hypothesis:")
print(specific)

print("\nFinal General Hypothesis:")
general = [g for g in general if g != ["?"] * len(specific)]
for g in general:
    print(g)
