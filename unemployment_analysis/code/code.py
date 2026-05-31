import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px

plt.style.use('ggplot')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "Unemployment in India.csv"
)

df = pd.read_csv(csv_path)

print(df.head())
# data cleaning