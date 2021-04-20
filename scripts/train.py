import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv("data/students.csv")
X = data[['Hours']]
y = data['Scores']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "models/student_model.pkl")
print("Model saved.")