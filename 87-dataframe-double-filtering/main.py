#Filter a DataFrame by applying two simultaneous logical conditions (e.g., value greater than X and category equal to Y).

#-Importing : The module
import pandas as pd

#-Creating : The DataFrame
framedata = pd.DataFrame({"first" : [46461, 84686, 252367,300, 111],
                         "second" : [200000, 198, 222,786,3535],
                         "third":[10000,600,20000,200,10000000000000000]})

#-Filtering : The data in two logical conditions
cond = framedata[(framedata["first"] > 3000) & (framedata["third"] > 3000)]

#-Displaying : The filtered data
print(cond)