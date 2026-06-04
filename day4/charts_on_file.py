import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load dataset
df = pd.read_csv("Fertilizer Prediction.csv")
output_dir = Path(__file__).parent / "graphs"
output_dir.mkdir(parents=True, exist_ok=True)

print(df.head())

# Figure 1: Numeric Histograms
fig1, axes1 = plt.subplots(2, 3, figsize=(18, 10))
axes1 = axes1.flatten()

axes1[0].hist(df["Temparature"], bins=10)
axes1[0].set_title("Temperature")

axes1[1].hist(df["Humidity "], bins=10)
axes1[1].set_title("Humidity")

axes1[2].hist(df["Moisture"], bins=10)
axes1[2].set_title("Moisture")

axes1[3].hist(df["Nitrogen"], bins=10)
axes1[3].set_title("Nitrogen")

axes1[4].hist(df["Potassium"], bins=10)
axes1[4].set_title("Potassium")

axes1[5].hist(df["Phosphorous"], bins=10)
axes1[5].set_title("Phosphorous")

fig1.suptitle("Numeric Distributions", fontsize=18)
fig1.tight_layout(rect=[0, 0.03, 1, 0.95])
fig1.savefig(output_dir / "numeric_distributions.png", dpi=200)
plt.close(fig1)

# Figure 2: Grouped Bar Charts
fig2, axes2 = plt.subplots(2, 3, figsize=(18, 10))
axes2 = axes2.flatten()

df.groupby("Soil Type")["Temparature"].mean().plot(kind="bar", ax=axes2[0])
axes2[0].set_title("Avg Temp by Soil")
axes2[0].set_xlabel("Soil Type")
axes2[0].set_ylabel("Temperature")

f = df.groupby("Soil Type")["Humidity "].mean()
f.plot(kind="bar", ax=axes2[1])
axes2[1].set_title("Avg Humidity by Soil")
axes2[1].set_xlabel("Soil Type")
axes2[1].set_ylabel("Humidity")

c = df.groupby("Crop Type")["Moisture"].mean()
c.plot(kind="bar", ax=axes2[2])
axes2[2].set_title("Avg Moisture by Crop")
axes2[2].set_xlabel("Crop Type")
axes2[2].set_ylabel("Moisture")

df["Fertilizer Name"].value_counts().plot(kind="bar", ax=axes2[3])
axes2[3].set_title("Fertilizer Count")
axes2[3].set_xlabel("Fertilizer")
axes2[3].set_ylabel("Count")

axes2[4].axis("off")
axes2[5].axis("off")

fig2.suptitle("Grouped Bar Charts", fontsize=18)
fig2.tight_layout(rect=[0, 0.03, 1, 0.95])
fig2.savefig(output_dir / "grouped_bar_charts.png", dpi=200)
plt.close(fig2)

# Figure 3: Scatter and Distribution Charts
fig3, axes3 = plt.subplots(2, 3, figsize=(18, 10))
axes3 = axes3.flatten()

axes3[0].scatter(df["Nitrogen"], df["Phosphorous"])
axes3[0].set_title("Nitrogen vs Phosphorous")
axes3[0].set_xlabel("Nitrogen")
axes3[0].set_ylabel("Phosphorous")

axes3[1].scatter(df["Temparature"], df["Humidity "])
axes3[1].set_title("Temperature vs Humidity")
axes3[1].set_xlabel("Temperature")
axes3[1].set_ylabel("Humidity")

axes3[2].scatter(df["Moisture"], df["Nitrogen"])
axes3[2].set_title("Moisture vs Nitrogen")
axes3[2].set_xlabel("Moisture")
axes3[2].set_ylabel("Nitrogen")

df["Soil Type"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=axes3[3])
axes3[3].set_title("Soil Type Distribution")
axes3[3].set_ylabel("")

df["Fertilizer Name"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=axes3[4])
axes3[4].set_title("Fertilizer Distribution")
axes3[4].set_ylabel("")

axes3[5].axis("off")

fig3.suptitle("Scatter and Distribution Charts", fontsize=18)
fig3.tight_layout(rect=[0, 0.03, 1, 0.95])
fig3.savefig(output_dir / "scatter_distribution_charts.png", dpi=200)
plt.close(fig3)

print(f"Saved graphs to: {output_dir}")
