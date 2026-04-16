Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Importing required libraries
import pandas as pd

#Creating the employee_details DataFrame
employee_details = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Engineering', 'Engineering', 'HR', 'Marketing']
    })
# Creating the employee_salaries DataFrame
employee_salaries = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Salary': [50000, 70000, 80000, 55000, 60000]
    })
# Creating the sales_region_1 DataFrame
sales_region_1 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['North', 'North', 'North', 'North', 'North'],
    'Sales': [250, 300, 200, 400, 350]
    })
# Creating the sales_region_2 DataFrame
sales_region_2 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['South', 'South', 'South', 'South', 'South'],
    'Sales': [300, 320, 280, 360, 310]
    })
# Display the datasets
print("Employee Details:")
Employee Details:
print(employee_details)
   EmployeeID     Name   Department
0         101    Alice           HR
1         102      Bob  Engineering
2         103  Charlie  Engineering
3         104    David           HR
4         105      Eva    Marketing
print("\nEmployee Salaries:")
print(employee_salaries)
SyntaxError: multiple statements found while compiling a single statement
print("\nEmployee Salaries:")

Employee Salaries:
print(employee_salaries)
   EmployeeID  Salary
0         101   50000
1         102   70000
2         103   80000
3         104   55000
4         105   60000
print("\nSales Region 1:")

Sales Region 1:
print(sales_region_1)
        Date Region  Sales
0 2024-01-01  North    250
1 2024-01-02  North    300
2 2024-01-03  North    200
3 2024-01-04  North    400
4 2024-01-05  North    350
print("\nSales Region 2:")

Sales Region 2:
print(sales_region_2)
        Date Region  Sales
0 2024-01-01  South    300
1 2024-01-02  South    320
2 2024-01-03  South    280
3 2024-01-04  South    360
4 2024-01-05  South    310

#Grouping
# Grouping by department and calculating average salary
avg_salary_per_dept = employee_details.merge(employee_salaries,on='EmployeeID').groupby('Department')['Salary'].mean()
print("\nAverage Salary per Department:")

Average Salary per Department:
print(avg_salary_per_dept)
Department
Engineering    75000.0
HR             52500.0
Marketing      60000.0
Name: Salary, dtype: float64
#Merging
# Merging two DataFrames on the EmployeeID column
merged_data = pd.merge(employee_details, employee_salaries, on='EmployeeID',how='inner')
print("\nMerged Employee Data:")

Merged Employee Data:
print(merged_data)
   EmployeeID     Name   Department  Salary
0         101    Alice           HR   50000
1         102      Bob  Engineering   70000
2         103  Charlie  Engineering   80000
3         104    David           HR   55000
4         105      Eva    Marketing   60000
#Joining
# Importing required libraries
import pandas as pd
# Creating the stock_prices DataFrame with 'Date' as the index
stock_prices = pd.DataFrame({
 'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
 'Price': [150, 155, 152, 158, 160]
 })
stock_prices.set_index('Date', inplace=True)
# Creating the market_volume DataFrame with 'Date' as the index
market_volume = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Volume': [1000, 1100, 1050, 1150, 1200]
    })
market_volume.set_index('Date', inplace=True)
# Display the datasets
print("Stock Prices Data:")
Stock Prices Data:
print(stock_prices)
            Price
Date             
2024-01-01    150
2024-01-02    155
2024-01-03    152
2024-01-04    158
2024-01-05    160
>>> print("\nMarket Volume Data:")

Market Volume Data:
>>> print(market_volume)
            Volume
Date              
2024-01-01    1000
2024-01-02    1100
2024-01-03    1050
2024-01-04    1150
2024-01-05    1200
>>> # Performing the join operation
>>> # Joining market_volume to stock_prices based on their index
>>> joined_data = stock_prices.join(market_volume, how='inner')
>>> print("\nJoined Stock Prices and Market Volume Data:")

Joined Stock Prices and Market Volume Data:
>>> print(joined_data)
            Price  Volume
Date                     
2024-01-01    150    1000
2024-01-02    155    1100
2024-01-03    152    1050
2024-01-04    158    1150
2024-01-05    160    1200
>>> #Concatenating:
>>> # Concatenating DataFrames vertically
>>> consolidated_sales = pd.concat([sales_region_1, sales_region_2], axis=0)
>>> print("\nConsolidated Sales Data:")

Consolidated Sales Data:
>>> print(consolidated_sales)
        Date Region  Sales
0 2024-01-01  North    250
1 2024-01-02  North    300
2 2024-01-03  North    200
3 2024-01-04  North    400
4 2024-01-05  North    350
0 2024-01-01  South    300
1 2024-01-02  South    320
2 2024-01-03  South    280
3 2024-01-04  South    360
4 2024-01-05  South    310
