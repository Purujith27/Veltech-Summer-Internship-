import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("Fertilizer Prediction.csv")

print(df.head())

print(df.tail())

print("Shape:", df.shape)

print("Columns:", df.columns)

print(df.dtypes)

print(df.isnull().sum())

print(df.describe())

label_encoders = {}

for col in df.select_dtypes(include='string').columns:

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    label_encoders[col] = le

target = df.columns[-1]

X = df.drop(target, axis=1)

y = df[target]

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

print("Training Records:", len(X_train))

print("Testing Records:", len(X_test))

sample = X.iloc[[0]]

prediction = model.predict(sample)

print("Sample input:", sample.to_dict(orient='records')[0])
print("Predicted Value:", prediction[0])