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
# AVERAGE UNEMPLOYMENT RATE
# =========================

avg_unemployment = df['Estimated Unemployment Rate (%)'].mean()

print(
    f"\nAverage Unemployment Rate: {avg_unemployment:.2f}%"
)

# =========================
# TOP 10 STATES
# =========================

state_unemployment = (
    df.groupby('Region')
    ['Estimated Unemployment Rate (%)']
    .mean()
    .sort_values(ascending=False)
)

print("\nTop 10 States by Unemployment Rate:")
print(state_unemployment.head(10))

# =========================
# BAR CHART
# =========================

plt.figure(figsize=(12,6))

state_unemployment.head(10).plot(
    kind='bar',
    color='crimson'
)

plt.title(
    "Top 10 States with Highest Unemployment Rate",
    fontsize=14
)

plt.xlabel("State")
plt.ylabel("Unemployment Rate (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()