import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("data/students.csv")
X = df[['Hours']]
y = df['Scores']

model = LinearRegression()
model.fit(X, y)
joblib.dump(model, "models/student_model.pkl")
print("Model trained and saved.")