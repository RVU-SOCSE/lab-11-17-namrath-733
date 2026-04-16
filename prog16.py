Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#a) Identify the trend of any variable using line chart from Matplotlib and Seaborn using line plot for 3Salary_Data.csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:/Users/RVUW291/Desktop/11prog_3Salary_Data.csv")
>>> plt.plot(df['YearsExperience'],df['Salary'])
[<matplotlib.lines.Line2D object at 0x0000020B296FFCB0>]
>>> plt.ylabel('YearsExperience')
Text(0, 0.5, 'YearsExperience')
>>> plt.xlabel('Index')
Text(0.5, 0, 'Index')
>>> plt.legend()

Warning (from warnings module):
  File "<pyshell#8>", line 1
UserWarning: No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
<matplotlib.legend.Legend object at 0x0000020B295E8D70>
>>> plt.show()
>>> sns.lineplot(y=df['YearsExperience'],x=df['Salary'])
<Axes: xlabel='Salary', ylabel='YearsExperience'>
>>> plt.show()
>>> #b) Visualize the relationship between two correlated columns using scatter plot
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> df = pd.read_csv(r"C:/Users/RVUW291/Desktop/11prog_3Salary_Data.csv")
>>> plt.ylabel('Salary')
Text(0, 0.5, 'Salary')
>>> plt.xlabel('YearsExperience')
Text(0.5, 0, 'YearsExperience')
>>> plt.legend()

Warning (from warnings module):
  File "<pyshell#19>", line 1
UserWarning: No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
<matplotlib.legend.Legend object at 0x0000020B29CE46E0>
>>> plt.show()
>>> sns.scatterplot(x = df['Salary'], y = df['YearsExperience'])
<Axes: xlabel='Salary', ylabel='YearsExperience'>
>>> plt.show()
