#Convert a complex dictionary with nested lists and tuples into a JSON string using dumps().
#Importing:
import json as j
#Complex Dict:
complexDict = {'Birds':('Pelican','Eagle'),'Species':['Bug',['Grasshooper', 'Spider'], 'Mammal',['Tiger','Lion']]}
#Dumping:
fn = './21-input-json-save/userData.json'
with open(fn,'w') as f:
    myJSON = j.dumps(complexDict,indent=4)
#Showing
print(myJSON)