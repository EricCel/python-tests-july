#Read an Excel file specifying a particular worksheet directly in a single line of code.

#-Import : The module
import pandas as pd, os

#-Getting : The file and worksheet
ex_file = pd.read_excel(os.path.join(os.path.dirname(__file__), 'Transaction_List.xlsx'), 'Transactions')

#-Loading : The excel
print(ex_file)