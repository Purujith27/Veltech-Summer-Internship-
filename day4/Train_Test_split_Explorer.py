import pandas as pd
import numpy as np
from pandas.api.types import is_string_dtype
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from pathlib import Path


dataset_path = Path(__file__).resolve().parent / "Fertilizer Prediction.csv"
df = pd.read_csv(dataset_path)


print("Dataset loaded from:", dataset_path)
print(df.head(), end="\n\n")
print("Dataset Shape:", df.shape, end="\n\n")
print("Columns:", list(df.columns), end="\n\n")
print(df.isnull().sum(), end="\n\n")
print(df.describe(), end="\n\n")

for col in df.columns:
    if is_string_dtype(df[col]) or df[col].dtype == object:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])

X = df.iloc[:, :-1]

y = df.iloc[:, -1]

for size in [0.1, 0.2, 0.3]:

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=size,
        random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)

    rmse = np.sqrt(mse)

    r2 = r2_score(y_test, y_pred)

    print("-" * 60)
    print(f"Test Size: {size:.0%}")
    print(f"Train Records: {len(X_train)}")
    print(f"Test Records:  {len(X_test)}")
    print(f"Coefficients: {np.round(model.coef_, 4)}")
    print(f"Intercept:    {model.intercept_:.4f}")
    print(f"MSE:          {mse:.4f}")
    print(f"RMSE:         {rmse:.4f}")
    print(f"R² Score:     {r2:.4f}")