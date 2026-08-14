#Use the .loc method to access the first row of a table and then a specific field within that row.

#-Importing : The module
import pandas as pd, os

#-Getting : The excel path
direction = os.path.dirname(__file__)
ex_path = os.path.join(direction, 'test-multiple-sheets.xlsx')

#-Loading : The file
ex_file = pd.read_excel(ex_path)

#-Accessing : Row and field
rower = ex_file.loc[0]['Time']

#-Displaying : The data
print(rower)