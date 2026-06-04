import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from pandas.api.types import is_string_dtype

df = pd.read_csv("Fertilizer Prediction.csv")

print(df.head())

print(df.tail())

print("Shape:", df.shape)

print("Columns:", df.columns)

print(df.dtypes)

print(df.isnull().sum())

print(df.describe())

for col in df.columns:

    if df[col].dtype == "object" or is_string_dtype(df[col]):

        encoder = LabelEncoder()

        df[col] = encoder.fit_transform(df[col].astype(str))

target = df.columns[-1]

features = ["Temparature", "Humidity ", "Moisture"]

for feature in features:

    X = df[[feature]]

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

    print("\nFeature:", feature)

    print("Coefficient:", model.coef_)

    print("Intercept:", model.intercept_)

    print("Training Records:", len(X_train))

    print("Testing Records:", len(X_test))

    print("MSE =", mse)

    print("RMSE =", rmse)

    print("R² Score =", r2)