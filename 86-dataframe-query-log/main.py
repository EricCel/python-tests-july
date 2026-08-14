#Create a plain text audit log that records a message every time you perform a query on your DataFrame.

#-Importing : The modules
import pandas as pd, os
from datetime import datetime as da

#-Getting : The excel file
ex_file = pd.read_excel(os.path.join(os.path.dirname(__file__), 'Transaction_List.xlsx'), 'Transactions')

#-Converting : Titles to lowercase
ex_file.rename(columns={i:i.lower() for i in ex_file.columns},inplace=True)

#-Getting : The log file
lo_file = os.path.join(os.path.dirname(__file__), 'History.log')

#-Making a query : In the file

#--User input : Index
query_index = int(input("Search in? : (Row index) ")) #Row
while True:
    if query_index in list(range(ex_file.shape[0])):
        break
    else:
        raise IndexError("Index out of row range!")

#--User input : Item, search for coincidences
#---Coincidences :
query_item = input("What are you searching for? : ").lower() #Column
for i in ex_file.columns.tolist():
    if query_item in i:
        query_item = i
#---Validator :
while True:
    if query_item in ex_file.columns.tolist():
        break
    else:
        raise ValueError("Element doesn't exists, try again")

#-Getting : The result
result = ex_file.loc[query_index][query_item] #Result

#-Saving : To file, using date, index, coincidence and found
with open(lo_file,'a') as f:
    f.write(f'{da.strftime(da.now(),'%m/%d/%Y')}-{query_index}-{query_item}-{result}\n')