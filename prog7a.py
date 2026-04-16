Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
# Creating a DataFrame from a dictionary
data = { 'Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [25, 30, 35, 40],
'Salary': [50000, 60000, 70000, 80000] }
df = pd.DataFrame(data)
print("DataFrame from Scratch:")
DataFrame from Scratch:
print(df)
      Name  Age  Salary
0    Alice   25   50000
1      Bob   30   60000
2  Charlie   35   70000
3    David   40   80000

# Adding a new column 'Bonus' (10% of Salary)
df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame after adding 'Bonus' column:")

DataFrame after adding 'Bonus' column:
print(df)
      Name  Age  Salary   Bonus
0    Alice   25   50000  5000.0
1      Bob   30   60000  6000.0
2  Charlie   35   70000  7000.0
3    David   40   80000  8000.0

import pandas as pd
# Reading data from a CSV file
df = pd.read_csv('1experience.csv')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    df = pd.read_csv('1experience.csv')
  File "C:\Users\RVUW291\AppData\Roaming\Python\Python314\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\RVUW291\AppData\Roaming\Python\Python314\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\RVUW291\AppData\Roaming\Python\Python314\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\RVUW291\AppData\Roaming\Python\Python314\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\RVUW291\AppData\Roaming\Python\Python314\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: '1experience.csv'
>>> 
>>> # Display the first 6 rows
>>> print("First 6 rows of the DataFrame:")
First 6 rows of the DataFrame:
>>> print(df.head(6))
      Name  Age  Salary   Bonus
0    Alice   25   50000  5000.0
1      Bob   30   60000  6000.0
2  Charlie   35   70000  7000.0
3    David   40   80000  8000.0
>>> 
>>> # Displaying column names and data types
>>> print("\nColumn names and data types:")

Column names and data types:
>>> print(df.info())
<class 'pandas.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Name    4 non-null      str    
 1   Age     4 non-null      int64  
 2   Salary  4 non-null      int64  
 3   Bonus   4 non-null      float64
dtypes: float64(1), int64(2), str(1)
memory usage: 260.0 bytes
None
