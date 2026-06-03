import pandas as pd

def eda_report(df):
    print("=" * 50)
    print("EDA REPORT")
    print("=" * 50)

    print("\n1. Shape of Dataset")
    print(df.shape)

    print("\n2. Missing Values")
    print(df.isnull().sum())

    print("\n3. Numerical Columns Summary")
    print(df.describe())

    print("\n4. Categorical Columns Summary")

    cat_cols = df.select_dtypes(include=['object'])

    for col in cat_cols.columns:
        print(f"\nColumn: {col}")
        print(cat_cols[col].value_counts())

# Load CSV file
df = pd.read_csv("Fertilizer Prediction.csv")

# Run EDA
eda_report(df)