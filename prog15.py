Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #a) Visualize correlation matrix using heatmap from Seaborn to enhance readability of 4laptops.csv
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> df2 = pd.read_csv(r"C:/Users/RVUW291/Desktop/10prog_4laptops.csv")
>>> sns.heatmap(df2.corr(numeric_only=True),annot=True)
<Axes: >
