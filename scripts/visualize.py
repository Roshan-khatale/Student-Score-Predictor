import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/students.csv")
plt.scatter(df['Hours'], df['Scores'])
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.title("Study Time vs Score")
plt.grid(True)
plt.show()