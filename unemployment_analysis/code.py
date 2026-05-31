import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Styling
plt.style.use('ggplot')

# =========================
# LOAD DATASET
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "Unemployment in India.csv"
)

df = pd.read_csv(csv_path)

print("\nDataset Loaded Successfully\n")
print(df.head())

# =========================
# DATA CLEANING
# =========================

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("\nColumn Names:")
print(df.columns)

# Remove extra spaces from all string columns
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype(str).str.strip()

# Convert Date column
df['Date'] = pd.to_datetime(
    df['Date'],
    dayfirst=True,
    errors='coerce'
)

# =========================
# CHECK MISSING VALUES
# =========================

print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# =========================
# BASIC INFORMATION
# =========================

print("\nDataset Info:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nSummary Statistics:")
print(df.describe())

# =========================
# TOP 10 STATES BAR CHART
# =========================
state_unemployment = ( 
    df.groupby('Region') ['Estimated Unemployment Rate (%)'] .mean() .sort_values(ascending=False) ) 
print("\nTop 10 States by Unemployment Rate:") 
print(state_unemployment.head(10))
top10 = state_unemployment.head(10)

plt.figure(figsize=(14, 8))

ax = sns.barplot(
    x=top10.values,
    y=top10.index,
    hue=top10.index,
    palette="viridis",
    legend=False
)

# Add value labels
for i, value in enumerate(top10.values):
    ax.text(
        value + 0.2,
        i,
        f"{value:.2f}%",
        va='center',
        fontsize=11,
        fontweight='bold'
    )

plt.title(
    "Top 10 States with Highest Unemployment Rate",
    fontsize=20,
    fontweight='bold'
)

plt.xlabel(
    "Average Unemployment Rate (%)",
    fontsize=14
)

plt.ylabel(
    "State",
    fontsize=14
)

plt.grid(axis='x', linestyle='--', alpha=0.4)

plt.tight_layout()

# Save graph
plt.savefig(
    "images/top10_unemployment_states.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()