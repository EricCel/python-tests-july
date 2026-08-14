#Retrieve the name of the customer or item that recorded the highest transaction from the loaded file.

#-Import : The module
import pandas as pd, os

#-Getting : The excel path
direction = os.path.dirname(__file__)
ex_path = os.path.join(direction, 'Transaction_List.xlsx')

#-Loading : The file
ex_file = pd.read_excel(ex_path)

#-Retrieving : The name of the customer or item
result = ex_file.loc[ex_file['Price'].idxmax()]
print(f'The client {result['Client Name']} has the highest transaction ({float(result['Price']):,.2f}), his item is : {result['Item Description']}')