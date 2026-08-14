#Find the entire row that contains the maximum value of a column using .idxmax() in combination with .loc.

#-Importing : The module
import pandas as pd

#-Creating : The DataFrame
my_daaah = pd.DataFrame({"Name" : ["Sound of the Sound", "Tragic Speedway", "Dust!Printer","AAAAAHGH!","NOTHING, A THEATRICAL EXPERIENCE"],
                         "Year" : ["2016", "1980", "2022","A","2026"],
                         "Recaudation":[10000,600,20000,200,10000000000000000]})

#-Finding : Row with max column
max_column_val = my_daaah.loc[my_daaah['Recaudation'].idxmax(0)]

#-Displaying : Max of recaudation
print(max_column_val)