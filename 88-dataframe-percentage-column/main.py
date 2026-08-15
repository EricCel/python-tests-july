#Calculate the percentage that each row represents relative to the total sum of a numeric column and add it as a new column.

#-Importing : The module
import pandas as pd, os, time

#-Creating : The DataFrame
framedata = pd.DataFrame({"first" : [10, 27, 38, 46, 56],
                         "second" : [29, 35, 74, 86, 11],
                         "third":[56, 22, 11, 2, 16]}) 

#-Displaying : The old DataFrame
print(framedata)

#-Creating : The function
def row_percentage(df):
    for row, row_n in zip(df.keys(), range(len(df.keys()))):
        percentage_row = [( item / df[row].sum() ) * 100 for item in df[row]]
        df.insert(row_n + row_n, f'{row} percentage', percentage_row)

    new_dat = pd.DataFrame({name:[df[name].sum()] for name in df.keys()})
    return pd.concat([df,new_dat],ignore_index=True)

#-Assigning : The modified DataFrame
framedata = row_percentage(framedata)

#-Displaying : The DataFrame
print(framedata)

#-Saving : To an excel because it looks messy in the terminal
direction = os.path.dirname(__file__)
ex_path = os.path.join(direction, f'{str(time.time()).replace('.','_')}.xlsx')
framedata.to_excel(ex_path)