#Manually create a Pandas DataFrame from a dictionary of lists (e.g., products, prices, and stock).

#-Importing : The module
import pandas as pd

#-Data : Dictionary of lists
dih_of_ligma = {'products':['soap','chicken','noodles'],'prices':[22.99,3.99,0.99],'stock':[75,34,86]}

#-Creating : The dataframe
dataF = pd.DataFrame(dih_of_ligma)
print(dataF)