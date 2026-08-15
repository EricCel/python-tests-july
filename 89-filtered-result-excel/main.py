#Export the result of a filtered DataFrame to a new Excel or CSV file.

#-Importing : The module
import pandas as pd, os, time

#-Creating : The DataFrame
framedata = pd.DataFrame({"first" : [46461, 84686, 252367,300, 111],
                         "second" : [200000, 198, 222,786,3535],
                         "third":[10000,600,20000,200,10000000000000000]})

#-Filtering : The data in two logical conditions
framedata = framedata[(framedata["first"] > 3000) & (framedata["third"] > 3000)]

#-Saving : To an excel
direction = os.path.dirname(__file__)
ex_path = os.path.join(direction, f'{str(time.time()).replace('.','_')}.xlsx')
framedata.to_excel(ex_path)