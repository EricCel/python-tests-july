#Read a .json file containing a list of objects and calculate the mean of a numerical property present in all of them.
#Importing
import json as j
#Getting list:
with open("./25-list-json-mean/products.json") as f:
    content = j.load(f)
    #Getting the mean
    avgPRICE = sum([list(i.values())[1] for i in content]) / len(content)
    print(f'The average price is {avgPRICE:\N{Sparkles}^20}')
