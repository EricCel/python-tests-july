#Implement a configuration manager that loads default settings from a JSON file if it does not exist, or reads them if it is already created.
import json as j
try:
    with open('./28-config-exist-manager/config.json','r') as f:
        data = j.load(f)
        print(f'Welcome back!, {data['name']} : {data['email']}')

except:
    template = ['name','email']
    data = [input(f'Welcome to Instant, to register, please insert your {i}: ') for i in template]

    with open('./28-config-exist-manager/config.json','w') as f:
            j.dump({i:j for i, j in zip(template,data)},f,indent=4)