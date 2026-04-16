Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
# Load the CSV file
df = pd.read_csv('C:/Users/RVUW291/Desktop/5prog_1experience.csv')
# Statistical summary of the data using describe()
description = df.describe()
# Calculating quantiles
quantiles = df['YearsExperience'].quantile([0.25, 0.5, 0.75])
# Calculating skewness and kurtosis
skewness = df['YearsExperience'].skew()
kurtosis = df['YearsExperience'].kurt()
>>> # Calculating value counts for unique values in the 'YearsExperience' column
>>> value_counts = df['YearsExperience'].value_counts()
>>> # Displaying the results
>>> print("Statistical Summary:\n", description)
Statistical Summary:
        YearsExperience
count         9.000000
mean          2.266667
std           0.839643
min           1.100000
25%           1.500000
50%           2.200000
75%           3.000000
max           3.200000
>>> print("\nQuantiles:\n", quantiles)

Quantiles:
 0.25    1.5
0.50    2.2
0.75    3.0
Name: YearsExperience, dtype: float64
>>> print("\nSkewness:", skewness)

Skewness: -0.18643041769017651
>>> print("Kurtosis:", kurtosis)
Kurtosis: -1.8530398729583881
>>> print("\nValue Counts:\n", value_counts)

Value Counts:
 YearsExperience
3.2    2
1.1    1
1.3    1
1.5    1
2.0    1
2.2    1
2.9    1
3.0    1
Name: count, dtype: int64
