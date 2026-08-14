#Filter a DataFrame to display only those rows where a numeric column exceeds a given threshold (e.g., Amount > 2000).

#-Importing : The module
import pandas as pd

#-Creating : The DataFrame
my_daaah = pd.DataFrame({"Name" : ["Sound of the Sound", "Tragic Speedway", "Dust!Printer","AAAAAHGH!"],
                         "Country" : ["Bolivia", "Spain", "Ifontknow","A"],
                         "Recaudation":[10000,600,20000,200]})

#-Displaying : The DataFrame with condition
print(my_daaah[my_daaah["Recaudation"] > 1000],'\n')
print(my_daaah[my_daaah["Recaudation"] > 10000],'\n')
print(my_daaah[my_daaah["Recaudation"] < 1000])