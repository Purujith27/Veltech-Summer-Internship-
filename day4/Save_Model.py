import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Read Dataset
df = pd.read_csv("Fertilizer Prediction.csv")

# 2. Display First 5 Rows
print("\nFirst 5 Rows:")
print(df.head())

# 3. Display Last 5 Rows
print("\nLast 5 Rows:")
print(df.tail())

# 4. Display Shape
print("\nDataset Shape:")
print(df.shape)

# 5. Display Column Names
print("\nColumn Names:")
print(df.columns)

# 6. Display Data Types
print("\nData Types:")
print(df.dtypes)

# 7. Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 8. Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# 9. Store Label Encoders
label_encoders = {}

# 10. Encode Categorical Columns
for col in df.columns:
    if df[col].dtype == "object" or df[col].dtype == "string":

        # 11. Create Encoder
        encoder = LabelEncoder()

        # 12. Fit and Transform
        df[col] = encoder.fit_transform(df[col])

        # 13. Store Encoder
        label_encoders[col] = encoder

# 14. Display Encoded Dataset
print("\nEncoded Dataset:")
print(df.head())

# 15. Select Features
X = df.iloc[:, :-1]

# 16. Select Target
y = df.iloc[:, -1]

# 17. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 18. Display Training Shape
print("\nTraining Data Shape:", X_train.shape)

# 19. Display Testing Shape
print("Testing Data Shape:", X_test.shape)

# 20. Create Model
model = LinearRegression()

# 21. Train Model
model.fit(X_train, y_train)

# 22. Predict Test Data
y_pred = model.predict(X_test)

# 23. Calculate MSE
mse = mean_squared_error(y_test, y_pred)

# 24. Calculate RMSE
rmse = np.sqrt(mse)

# 25. Calculate R² Score
r2 = r2_score(y_test, y_pred)

# 26. Display Coefficients
print("\nCoefficients:")
print(model.coef_)

# 27. Display Intercept
print("\nIntercept:")
print(model.intercept_)

# 28. Print MSE
print("\nMSE:", mse)

# 29. Print RMSE
print("RMSE:", rmse)

# 30. Print R² Score
print("R² Score:", r2)

# 31. Save Model as PKL File
with open("fertilizer_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel Saved Successfully!")

# 32. Check PKL File Exists
if os.path.exists("fertilizer_model.pkl"):
    print("PKL File Created Successfully!")
else:
    print("PKL File Creation Failed!")

# 33. Load Model
with open("fertilizer_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

print("Model Loaded Successfully!")

# 34. Sample 1
sample1 = [X.iloc[0].values]

# 35. Sample 2
sample2 = [X.iloc[1].values]

# 36. Sample 3
sample3 = [X.iloc[2].values]

# 37. Predict Sample 1
pred1 = loaded_model.predict(sample1)

# 38. Predict Sample 2
pred2 = loaded_model.predict(sample2)

# 39. Predict Sample 3
pred3 = loaded_model.predict(sample3)

# 40. Display Predictions
print("\nPrediction 1:", pred1[0])
print("Prediction 2:", pred2[0])
print("Prediction 3:", pred3[0])

# 41. Display Completion Message
print("\nProgram Executed Successfully!")