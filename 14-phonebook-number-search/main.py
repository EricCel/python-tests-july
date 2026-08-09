#Implement a phone book that allows searching for a contact by name or phone number.
phonebook = [("Robert","1-305-1234567"),("Joseph","1-305-5135353"),("Albert","1-305-7575753"),("Gaster","1-305-15313512")]

def contactSearch(phonebook, data):
    for i in phonebook:
        if data in i: result = i
        else: continue

    try: return result
    except: return "ERROR, DATA DOESN'T EXISTS"
    
print(contactSearch(phonebook,"1-305-5135353"))