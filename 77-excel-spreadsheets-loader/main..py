#Load an Excel file containing spreadsheets and print the names of all its tabs (sheets).

#-Importing : The module
import pandas as pd, os

#-Getting : The excel path
direction = os.path.dirname(__file__)
ex_path = os.path.join(direction, 'test-multiple-sheets.xlsx')

#-Loading : The file
ex_file = pd.ExcelFile(ex_path)

#-Displaying : The names of all his sheets
print(ex_file.sheet_names)