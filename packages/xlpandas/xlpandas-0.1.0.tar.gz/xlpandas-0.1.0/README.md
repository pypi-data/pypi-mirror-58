# xlPandas

Read and write Excel xlsx using pandas/openpyxl without destroying formatting.

Sometimes you have a nicely formatted worksheet, but you'd like to work with it
using [pandas](https://pypi.org/project/pandas/), or perhaps you want to write
data to an Excel template.

Pandas can read and write Excel files using `xlrd`, but treats them like csvs.
xlPandas uses [openpyxl](https://pypi.org/project/openpyxl/) to access data
while preserving template formatting, macros, and other worksheet attributes.

## Install

`pip install xlpandas`

## Example

``` python

import xlPandas as xpd

# Read excel file
df = xpd.read_file('template.xlsx', skiprows=2)
print(df.columns)

# Modify dataframe
df['new_column'] = True

# Access openpyxl worksheet
sheet = df.to_sheet()
sheet.cell(1,1) = 'title'

# From openpyxl worksheet
df = xpd.xlDataFrame(sheet)

# Write file
df.to_file('out.xlsx')

```

