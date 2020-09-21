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

####################################
#   Pivot Tables
pivot = pd.pivot_table(df,
                       index=[df['Date'].dt.month, 'Type'],
                       columns='Region',
                       values='Amount',
                       aggfunc='sum',
                       fill_value=0)
print(pivot)

# Returns:
# Region       East  West
# Date Type
# 1    Green   3682     0
#      Orange  2340  2697
# 2    Green   3205  1685
#      Orange  2349  1618
# 3    Green   3875  1093
#      Orange   436  3998

print("contcat")
df = pd.concat(pd.read_excel(url, sheet_name=None, skiprows=3), ignore_index=True)
