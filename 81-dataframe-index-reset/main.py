#Reset the index of a DataFrame to restore it to its default sequential numeric state.
#-Importing : The module
import pandas as pd

#-Creating : The DataFrame
new_df = pd.DataFrame({'Name':['Dennis','Carlos','Person'],
                       'Plataform':['Youtube','Instagram','Tik Tok'], 
                       'Followers':[100000,600000,450000]})

#-Setting : Text column as index
new_df.set_index('Name',inplace=True)
new_df.index.name = None

#-Resetting : The index
new_df.reset_index(inplace=True)
new_df.rename({'index':'Name'},axis=1,inplace=True)

#-Displaying : The dataframe
print(new_df)