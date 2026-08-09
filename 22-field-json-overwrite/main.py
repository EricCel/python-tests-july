#Read an existing .json file, modify one of its fields in memory, and overwrite the original file.

#Importing:
import json as j, random as r

#Loading:
fn = './22-field-json-overwrite/userData.json'
with open(fn,'r') as f:
    content = j.load(f)

#Dumping:
with open(fn,'w') as f:
    content['userName'] = str(r.randint(0,32))
    j.dump(content, f)

#Showing:
print(content)