import csv
import random

with open("price_predictor.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["size_sqft", "bedrooms", "age", "distance_city", "price"])

    for i in range(100):
        size_sqft = random.randint(1000, 4500)
        bedrooms = random.randint(2, 4)
        age = random.randint(18, 70)
        distance_city = random.randint(5, 20)
        price = random.randint(150000, 700000)

        writer.writerow([size_sqft,bedrooms,age,distance_city,price])
print("CSV file created successfully")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

files = pd.read_csv("price_predictor.csv")
print(files.describe())

f = np.median(files["price"])
print(f"Median price value: {f}")

plt.hist(files['price'], bins=20)
plt.xlabel("price")
plt.ylabel("frequency")
plt.show()

scaler = StandardScaler()
x = files[['price']]
scaled = scaler.fit_transform(x)
print(f"standardization price values: {scaled}")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = files[['size_sqft', 'bedrooms', 'age', 'distance_city']]
y = files['price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(predictions)

from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score

print("MAE:", mean_absolute_error(y_test, predictions))
print("RMSE:", root_mean_squared_error(y_test, predictions))
print("R²:", r2_score(y_test, predictions))

