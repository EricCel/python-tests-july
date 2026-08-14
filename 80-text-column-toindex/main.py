#Set a text column as the index of a DataFrame and look up an entire row using that new index.

#-Importing : The module
import pandas as pd

#-Creating : The DataFrame
new_df = pd.DataFrame({'Name':['Dennis','Carlos','Person'],
                       'Plataform':['Youtube','Instagram','Tik Tok'], 
                       'Followers':[100000,600000,450000]})

#-Setting : Text column as index
new_df.set_index('Name',inplace=True)
new_df.index.name = None

#-Displaying : The dataframe
print(new_df)