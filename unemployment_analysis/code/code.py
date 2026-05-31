import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px

plt.style.use('ggplot')

# Load data set
df = pd.read_csv("Unemployment in India.csv")

df.head()