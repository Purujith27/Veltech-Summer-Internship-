import pandas as pd

# Load CSV file
df = pd.read_csv("Fertilizer Prediction.csv")

print("=== Missing Values Before Cleaning ===")
print(df.isnull().sum())

# Fill numeric columns with mean
numeric_cols = df.select_dtypes(include=['number']).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# Fill text/object columns with 'Unknown'
object_cols = df.select_dtypes(include=['object']).columns

for col in object_cols:
    df[col] = df[col].fillna("Unknown")

print("\n=== Missing Values After Cleaning ===")
print(df.isnull().sum())

if df.isnull().sum().sum() == 0:
    print("\nNo missing values remain.")
else:
    print("\nSome missing values still exist.")  