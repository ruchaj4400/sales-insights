import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_missing_values(df: pd.DataFrame):
    """Bar plot of missing values by column."""
    missing = df.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    if missing.empty:
        print("No missing values.")
        return
    plt.figure(figsize=(8,4))
    sns.barplot(x=missing.values, y=missing.index)
    plt.title("Missing Values by Column")
    plt.show()

def plot_correlation(df: pd.DataFrame):
    """Heatmap of correlations."""
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()
