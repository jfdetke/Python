#!/usr/bin/env python3
import pandas as pd
url = 'https://github.com/datagy/mediumdata/raw/master/exceltopandas.xlsx'
url = 'file:///Users/jdetke/Projects/foobar/exceltopandas.xlsx'
excel_file = pd.ExcelFile(url)

print(excel_file.sheet_names)

# Returns: ['January', 'February', 'March']

df = pd.DataFrame()

for sheet in excel_file.sheet_names:
    temp_df = pd.read_excel(url, skiprows=3)
    df = df.append(temp_df, ignore_index=True)

print(df.head())

# Returns:
#        Date    Type Region  Amount
#0 2020-01-01  Orange   West    1023
#1 2020-01-03   Green   East    1034
#2 2020-01-06   Green   East     987
#3 2020-01-08  Orange   West     645
#4 2020-01-13   Green   East    1203
