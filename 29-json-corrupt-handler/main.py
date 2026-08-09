#Write a script that checks if a data .json file is corrupted using an exception handling block.

import json as j

try:
    with open('./29-json-corrupt-handler/descriptions.json', 'r') as f:
        content = j.load(f)
        print(content)
except:
    raise Exception('Json file is corrupt, bad-written or inexistent, please, insert a valid file')