Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Visualize the relationship between categorical and a numerical column using bar plot for 5ds_salaries.csv
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> df4 = pd.read_csv(r"C:/Users/RVUW291/Desktop/14prog_5ds_salaries.csv")
>>> plt.bar(df4['experience_level'], df4['salary_in_usd'], width = 0.5) #edgecolor='white',linewidth=0.4)
<BarContainer object of 3755 artists>
>>> plt.show()
>>> sns.barplot(x=df4['experience_level'], y=df4['salary_in_usd'])
<Axes: xlabel='experience_level', ylabel='salary_in_usd'>
