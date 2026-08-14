#Select a specific column from a DataFrame and print its sum, average, and maximum value.

#-Importing : The module
import pandas as pd, os

#-Creating : The dataframe
daer = {'biology':[6,12,15],'language':[16,12,16],'mathematics':[11,5,4]}
my_datf = pd.DataFrame(daer)
#-Calculate : Sum, average, and maximum
sum_column = my_datf.sum(1)[0] #biology column
mean_column = my_datf.mean(1)[0] #biology column
max_column = my_datf.max(1)[0] #biology column

#-Display : The results
print(sum_column)
print(mean_column)
print(max_column)