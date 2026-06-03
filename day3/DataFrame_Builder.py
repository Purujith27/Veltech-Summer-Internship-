import pandas as pd

data = {
    "Name": ["Arun", "Priya", "Rahul", "Meena", "Karthik"],
    "Age": [18, 19, 18, 20, 19],
    "City": ["Chennai", "Madurai", "Coimbatore", "Salem", "Trichy"],
    "Marks": [85, 72, 90, 65, 78]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nShape:", df.shape)
print("\nData Types:")
print(df.dtypes)

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("\nUpdated DataFrame:")
print(df)