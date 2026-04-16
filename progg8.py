Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
... # Load the CSV file
>>> df = pd.read_csv('"C:\Users\RVUW291\Desktop\5prog_1experience.csv"')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 3-4: truncated \UXXXXXXXX escape
>>> df = pd.read_csv('C:\Users\RVUW291\Desktop\5prog_1experience.csv')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> df = pd.read_csv('C:/Users/RVUW291/Desktop/5prog_1experience.csv')
>>> 
>>> # Displaying the basic central tendencies and dispersion metrics
>>> mean_value = df['YearsExperience'].mean()
>>> median_value = df['YearsExperience'].median()
>>> mode_value = df['YearsExperience'].mode()[0]
>>> min_value = df['YearsExperience'].min()
>>> max_value = df['YearsExperience'].max()
... variance_value = df['YearsExperience'].var()
SyntaxError: multiple statements found while compiling a single statement
>>> max_value = df['YearsExperience'].max()
>>> variance_value = df['YearsExperience'].var()
>>> std_dev_value = df['YearsExperience'].std()
>>> 
>>> # Printing the results
>>> print(f"Mean: {mean_value}")
Mean: 2.266666666666667
>>> print(f"Median: {median_value}")
Median: 2.2
>>> print(f"Mode: {mode_value}")
Mode: 3.2
>>> print(f"Minimum: {min_value}")
Minimum: 1.1
>>> print(f"Maximum: {max_value}")

>>> print(f"Variance: {variance_value}")
Variance: 0.7050000000000001
>>> print(f"Standard Deviation: {std_dev_value}")
Standard Deviation: 0.8396427811873333
