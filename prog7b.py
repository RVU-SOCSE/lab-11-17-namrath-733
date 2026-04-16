Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
# Loading a CSV file into a DataFrame
df=
SyntaxError: invalid syntax
df=pd.read_csv(r"C:\Users\RVUW291\Desktop\7prog_6Mcd_null_values.csv")
print("Original DataFrame:")
Original DataFrame:
df
    Year  McDonalds_Revenue_$Billion  Growth_rate_percent   Q1   Q2   Q3   Q4
0   1999                        13.3                  NaN  NaN  NaN  NaN  NaN
1   2000                        14.2                  7.0  NaN  NaN  NaN  NaN
2   2001                        14.9                  4.0  NaN  NaN  NaN  NaN
3   2002                        15.4                  4.0  NaN  NaN  NaN  3.0
4   2003                        17.1                 11.0  3.8  4.3  4.5  4.6
5   2004                        18.6                  8.0  4.4  4.7  4.9  4.5
6   2005                        19.1                  3.0  4.8  5.1  5.3  3.9
7   2006                        20.9                  9.0  4.9  5.4  5.5  5.1
8   2007                        22.8                  9.0  5.3  5.8  5.9  5.8
9   2008                        23.5                  3.0  5.6  6.1  6.3  5.6
10  2009                        22.7                 -3.0  5.1  5.6  6.0  6.0
11  2010                        24.1                  6.0  5.6  5.9  6.3  6.2
12  2011                        27.0                 12.0  6.1  6.9  7.2  6.8
13  2012                        27.6                  2.0  6.5  6.9  7.2  7.0
14  2013                        28.1                  2.0  6.6  7.1  7.3  7.1
15  2014                        27.4                 -2.0  6.7  7.2  7.0  6.6
16  2015                        25.4                 -7.0  6.0  6.5  6.6  6.3
17  2016                        24.6                 -3.0  5.9  6.3  6.4  6.0
18  2017                        22.8                 -7.0  5.7  6.0  5.8  5.3
19  2018                        21.3                 -7.0  5.1  5.4  5.4  5.4
20  2019                        21.4                  1.0  5.0  5.3  5.6  5.4
21  2020                        19.2                -10.0  4.7  3.8  5.4  5.3
22  2021                        23.2                 21.0  5.1  5.9  6.2  6.0
23  2022                        23.2                  0.0  5.7  5.7  5.9  5.9

# Identifying missing values
print("\nMissing values in the DataFrame:")

Missing values in the DataFrame:
print(df.isnull().sum())
Year                          0
McDonalds_Revenue_$Billion    0
Growth_rate_percent           1
Q1                            4
Q2                            4
Q3                            4
Q4                            3
dtype: int64

# Filling missing values in the 'Age' column with the mean
df['Q1'].fillna(df['Q1'].mean(), inplace=True)

Warning (from warnings module):
  File "<pyshell#12>", line 1
ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series through chained assignment using an inplace method.
Such inplace method never works to update the original DataFrame or Series, because the intermediate object on which we are setting values always behaves as a copy (due to Copy-on-Write).

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' instead, to perform the operation inplace on the original object, or try to avoid an inplace operation using 'df[col] = df[col].method(value)'.

See the documentation for a more detailed explanation: https://pandas.pydata.org/pandas-docs/stable/user_guide/copy_on_write.html
0     5.43
1     5.43
2     5.43
3     5.43
4     3.80
5     4.40
6     4.80
7     4.90
8     5.30
9     5.60
10    5.10
11    5.60
12    6.10
13    6.50
14    6.60
15    6.70
16    6.00
17    5.90
18    5.70
19    5.10
20    5.00
21    4.70
22    5.10
23    5.70
Name: Q1, dtype: float64
>>> print("\nDataFrame after filling missing values in 'Q1' column:")

DataFrame after filling missing values in 'Q1' column:
>>> df
    Year  McDonalds_Revenue_$Billion  Growth_rate_percent   Q1   Q2   Q3   Q4
0   1999                        13.3                  NaN  NaN  NaN  NaN  NaN
1   2000                        14.2                  7.0  NaN  NaN  NaN  NaN
2   2001                        14.9                  4.0  NaN  NaN  NaN  NaN
3   2002                        15.4                  4.0  NaN  NaN  NaN  3.0
4   2003                        17.1                 11.0  3.8  4.3  4.5  4.6
5   2004                        18.6                  8.0  4.4  4.7  4.9  4.5
6   2005                        19.1                  3.0  4.8  5.1  5.3  3.9
7   2006                        20.9                  9.0  4.9  5.4  5.5  5.1
8   2007                        22.8                  9.0  5.3  5.8  5.9  5.8
9   2008                        23.5                  3.0  5.6  6.1  6.3  5.6
10  2009                        22.7                 -3.0  5.1  5.6  6.0  6.0
11  2010                        24.1                  6.0  5.6  5.9  6.3  6.2
12  2011                        27.0                 12.0  6.1  6.9  7.2  6.8
13  2012                        27.6                  2.0  6.5  6.9  7.2  7.0
14  2013                        28.1                  2.0  6.6  7.1  7.3  7.1
15  2014                        27.4                 -2.0  6.7  7.2  7.0  6.6
16  2015                        25.4                 -7.0  6.0  6.5  6.6  6.3
17  2016                        24.6                 -3.0  5.9  6.3  6.4  6.0
18  2017                        22.8                 -7.0  5.7  6.0  5.8  5.3
19  2018                        21.3                 -7.0  5.1  5.4  5.4  5.4
20  2019                        21.4                  1.0  5.0  5.3  5.6  5.4
21  2020                        19.2                -10.0  4.7  3.8  5.4  5.3
22  2021                        23.2                 21.0  5.1  5.9  6.2  6.0
23  2022                        23.2                  0.0  5.7  5.7  5.9  5.9
