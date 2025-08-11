# Needed imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr # linear
from scipy.stats import spearmanr # non-linear

# Load exported data into data frame for correlation calculation
df = pd.read_csv(r'C:\Users\USERNAME\Desktop\Portfolio\export.csv')

# Verify exported data structure
print(df.head())

# Check for null values in exported data
print(df.isnull().sum())

# Calculate Pearson correlation and p-value
r, p_value = pearsonr(df['totalsales'], df['commissionpct'])

print(f"Pearson correlation: {r:.4f} (p-value: {p_value:.6f})")

# Calculate Spearman correlation and p-value
rho, p_value = spearmanr(df['totalsales'], df['commissionpct'])

print(f"Spearman correlation: {rho:.4f} (p-value: {p_value:.4g})")

# Compute correlation matrix for heatmap
corr_matrix = df[['totalsales', 'commissionpct']].corr()

# Create heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# Non-linear trend scatterplot (Lowess = true)
sns.lmplot(
    x='totalsales', 
    y='commissionpct', 
    data=df, 
    lowess=True,
    height=6, 
    aspect=1.3, 
    scatter_kws={'alpha': 0.6}
)

# Graph non-linear trend line for scatterplot
plt.title("Nonlinear Trend: Total Sales vs. Commission %")
plt.xlabel("Total Sales")
plt.ylabel("Commission %")
plt.tight_layout()
plt.show()