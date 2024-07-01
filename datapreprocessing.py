import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
# Load Data
walmart = pd.read_csv('A:\csi_assignments\Data Pre-processing and Feature Engineering\Walmart.csv')

# Print the number of rows and columns
print("Number of rows and columns:", walmart.shape)

# Check for missing values
print("Missing values:\n", walmart.isnull().sum())

# Convert Data Types
walmart['Weekly_Sales'] = walmart['Weekly_Sales'].astype(float)
walmart['Holiday_Flag'] = walmart['Holiday_Flag'].astype(int)
walmart['Temperature'] = walmart['Temperature'].astype(float)
walmart['Fuel_Price'] = walmart['Fuel_Price'].astype(float)
walmart['CPI'] = walmart['CPI'].astype(float)
walmart['Unemployment'] = walmart['Unemployment'].astype(float)

# Define threshold/outlier
def detect_outliers(df, columns):
    outliers = {}
    for column in columns:
        lower_percentile = df[column].quantile(0.01)
        upper_percentile = df[column].quantile(0.99)
        outliers[column] = {
            "Lower Bound": lower_percentile,
            "Upper Bound": upper_percentile,
            "Outliers": df[(df[column] < lower_percentile) | (df[column] > upper_percentile)][column].values
        }
    return outliers

# Columns to check for outliers
columns_to_check = ['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']

# Detect outliers
outliers_info = detect_outliers(walmart, columns_to_check)

# Print outliers
for column, info in outliers_info.items():
    print(f"Outliers for {column}:")
    print(f"  Lower Bound: {info['Lower Bound']}")
    print(f"  Upper Bound: {info['Upper Bound']}")
    print(f"  Outliers: {info['Outliers']}")

# Remove data not lying in the range of outliers
def remove_outliers(df, columns):
    for column in columns:
        lower_percentile = df[column].quantile(0.01)
        upper_percentile = df[column].quantile(0.99)
        df = df[(df[column] >= lower_percentile) & (df[column] <= upper_percentile)]
    return df

# Remove outliers
walmart_cleaned = remove_outliers(walmart, columns_to_check)

# Print the number of rows and columns after removing outliers
print("Number of rows and columns after removing outliers:", walmart_cleaned.shape)

# Parse Dates and Feature Engineering
walmart_cleaned['Date'] = pd.to_datetime(walmart_cleaned['Date'], format='%d-%m-%Y')
walmart_cleaned['Month'] = walmart_cleaned['Date'].dt.month
walmart_cleaned['Year'] = walmart_cleaned['Date'].dt.year

# Normalize/Standardize Data (if required), Standardize 'Temperature'
walmart_cleaned['Temperature_Standardized'] = (walmart_cleaned['Temperature'] - walmart_cleaned['Temperature'].mean()) / walmart_cleaned['Temperature'].std()

#print(walmart_cleaned.to_string())

#boxplots
plt.figure(figsize=(15, 10))
for i, column in enumerate(columns_to_check, 1):
    plt.subplot(2, 3, i)
    sns.boxplot(y=walmart_cleaned[column])
    plt.title(f'Boxplot of {column}')
plt.tight_layout()
plt.show()

# Step 9: Determine Z-scores and print the outliers based on Z-scores
z_scores = walmart_cleaned[columns_to_check].apply(zscore)
outliers_z = (z_scores.abs() > 3).any(axis=1)
print("Z-score based outliers:")
print(walmart_cleaned[outliers_z])

# Display the cleaned DataFrame without Z-score outliers
walmart_cleaned_no_outliers = walmart_cleaned[~outliers_z]
#print(walmart_cleaned_no_outliers.to_string())
print(walmart_cleaned_no_outliers.head())
