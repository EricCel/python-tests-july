#Request user data in the console and save it to a .json file formatted with indentation.
import json as j

#User, name, birthday, favorite color, gender
template = ['userName','mail','birthday','favorite_color','gender']
data = dict([(template[template.index(i)],input(f'insert your {i}')) for i in template])

#Dump to Json:
fn = './21-input-json-save/userData.json'
with open(fn,'w') as f:
     j.dump(data,f,indent=4)