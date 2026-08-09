#Simulate a login system that validates whether a password is longer than 8 characters and contains no spaces.
password = 'Toad!@'

def validation(passW):
    return "Not valid!" if password.count(" ") > 0 or len(password) < 8 else "Accepted!"

print(validation(password))