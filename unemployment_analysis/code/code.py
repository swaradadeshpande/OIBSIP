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