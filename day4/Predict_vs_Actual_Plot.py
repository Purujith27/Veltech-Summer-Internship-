import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("Fertilizer Prediction.csv")

print(df.head())

print(df.tail())

print("Shape:", df.shape)

print("Columns:", df.columns)

print(df.dtypes)

print(df.isnull().sum())

print(df.describe())

for col in df.columns:

    if df[col].dtype == "object":

        le = LabelEncoder()

        df[col] = le.fit_transform(df[col])

X = df.iloc[:, :-1]

y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

print("Coefficients:", model.coef_)

print("Intercept:", model.intercept_)

print("RMSE:", rmse)

print("R² Score:", r2)

plt.figure(figsize=(8,6))

plt.scatter(y_test, y_pred, label="Predictions")

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--',
    label="Ideal Line"
)

plt.xlabel("Actual Values")

plt.ylabel("Predicted Values")

plt.title("Actual vs Predicted Values")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.show()