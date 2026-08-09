#Create a data converter: read a .json file and manually write its equivalent content in Comma-Separated Values (CSV) format.
import json as js, pandas as pd, os
fn = './27-json-csv-converter/file.json'
with open(fn,'r') as f: 
    content = pd.DataFrame(js.load(f))

content.to_csv(fn, index=False)
os.rename(fn,'./27-json-csv-converter/file.csv')