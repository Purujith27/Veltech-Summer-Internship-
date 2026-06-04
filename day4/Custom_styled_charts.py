import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Fertilizer Prediction.csv")

print(df.head())

print("Shape:", df.shape)

print(df.columns)

print(df.isnull().sum())

grouped = df.groupby("Soil Type")

avg_temp = grouped["Temparature"].mean()

plt.figure(figsize=(10,6))

plt.bar(avg_temp.index, avg_temp.values)

mean_temp = df["Temparature"].mean()

plt.axhline(
    y=mean_temp,
    linestyle="--",
    linewidth=2,
    label=f"Mean Temp = {mean_temp:.2f}"
)

plt.title("Average Temperature by Soil Type")

plt.xlabel("Soil Type")

plt.ylabel("Temperature")

plt.xticks(rotation=45)

plt.grid(True)

plt.text(
    0,
    mean_temp + 1,
    f"Mean = {mean_temp:.2f}"
)

plt.legend()

plt.tight_layout()

plt.show()