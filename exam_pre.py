import csv, random, pandas as pd, matplotlib.pyplot as plt, numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error

with open("exampredictor.csv", 'w', newline="") as file:
    writer = csv.writer(file)

    writer.writerow(['study_hours', 'attendance', 'previous_score', 'sleep_hours', 'assignments_completed', 'final_score'])

    for i in range(150):
        study_hours = random.randint(2, 8)
        attendance = random.randint(60, 95)
        previous_score = random.randint(45, 90)
        sleep_hours = random.randint(6, 8)
        assignments_completed = random.randint(4, 10)
        final_score = random.randint(48, 96)

        writer.writerow([study_hours, attendance, previous_score, sleep_hours, assignments_completed, final_score])
print("CSV successfully created.")

x = pd.read_csv("exampredictor.csv")
# print(x)

target = x['final_score']
features = x[['study_hours', 'attendance', 'previous_score', 'sleep_hours', 'assignments_completed']]
print(f"Median: {target.median()}")
print(f"Variance: {target.var()}")
print(f"Mode: {target.mode()}")
print(target.describe())

# j = stats.mode(target)
# print(f"This is for j: {j}")

x.hist(figsize=(12,8))
plt.tight_layout()
# plt.show()

scalar = StandardScaler()
targets = x[['final_score']]
x_target = scalar.fit_transform(targets)
x_test = scalar.transform(targets)
print(f"standardization values: {x_target}")
# print()
# print(x_test)

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
linear =  LinearRegression()

linear.fit(X_train, y_train)
prediction = linear.predict(X_test)
# print(prediction)

print(f"MAE: {mean_absolute_error(y_test, prediction)}")
print(f"RMSE: {root_mean_squared_error(y_test, prediction)}")
print(f"R²_score: {r2_score(y_test, prediction)}")

plt.scatter(y_test, prediction)

plt.xlabel("Actual Score")
plt.ylabel("Predicted Score")
plt.title("Actual vs Predicted Exam Scores")

plt.show()