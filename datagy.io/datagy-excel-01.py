#!/usr/bin/env python3
import pandas as pd
url = 'https://github.com/datagy/mediumdata/raw/master/exceltopandas.xlsx'
url = 'file:///Users/jdetke/Projects/foobar/exceltopandas.xlsx'
excel_file = pd.ExcelFile(url)

print(excel_file.sheet_names)

# Returns: ['January', 'February', 'March']
