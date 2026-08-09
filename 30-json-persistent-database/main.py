#Simulate a simple persistent database by saving and loading the state of an inventory in JSON when starting and closing the program.
import json as j
try:
    with open('./30-json-persistent-database/database.json','r') as f:
        data = j.load(f)
        print(data)

    template = ['username', 'email','country','birthday','gender']
    assigment = [input(f'Welcome to Instant, to register, please insert your {i}: ') for i in template]
    
    with open('./30-json-persistent-database/database.json','w') as f:
        appending = data.append({i:j for i, j in zip(template,assigment)})
        j.dump(data,f,indent=4)

except:
    template = ['username', 'email','country','birthday','gender']
    assigment = [input(f'Welcome to Instant, to register, please insert your {i}: ') for i in template]
    information = [{i:j for i, j in zip(template,assigment)}]

    with open('./30-json-persistent-database/database.json','w') as f:
            j.dump(information,f,indent=4)