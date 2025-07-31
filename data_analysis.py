import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
print("Loading dataset...")
df = pd.read_csv('sales.csv')  # Change filename if needed

# Display first 5 rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Display dataset info
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:\n")
print(df.describe())

# Calculate average of 'Sales'
avg_sales = df['Sales'].mean()
print(f"\nAverage Sales: {avg_sales:.2f}")

# -------------------- Visualization --------------------

# Bar Chart: Average Sales per Category
plt.figure(figsize=(10, 6))
df.groupby('Category Name')['Sales'].mean().sort_values().plot(kind='barh', color='skyblue')
plt.title('Average Sales per Category')
plt.xlabel('Average Sales')
plt.ylabel('Category')
plt.tight_layout()
plt.show()

# Scatter Plot: Sales vs Profit Per Order
plt.figure(figsize=(8, 6))
plt.scatter(df['Profit Per Order'], df['Sales'], alpha=0.5, color='orange')
plt.title('Sales vs Profit Per Order')
plt.xlabel('Profit Per Order')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# Heatmap: Correlation matrix
plt.figure(figsize=(10, 8))
numeric_cols = df.select_dtypes(include=['float64', 'int64'])  # Only numeric
corr_matrix = numeric_cols.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()
