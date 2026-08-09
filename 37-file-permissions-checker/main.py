#Check the read, write, and execute permissions of a specific file with os.access().

#-Importing:
import os

#-Checker:
def fCheck(file):
    for permission, state in zip(['Exists','Executable','Writable','Readable'],range(4)):
        print(f'{permission}?:{os.access(file,state)}')

#-Display:
fCheck(__file__)