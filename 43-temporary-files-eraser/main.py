#Create a routine that cleans up or deletes all temporary files created in a specific folder that are older than 7 days.

#-Importing:
import datetime as dt, random as ra, os

#-Setting Directory:
myDir = os.path.dirname(__file__)

with open(os.path.join(myDir,f'{str(dt.datetime.now().timestamp()).replace('.','_')}.temp'),'w') as f:
    f.write('USERUSER')

#-Creating Function:
def tempRoutine(directory):
    files = os.listdir(directory)
    for i in files:
        file = os.path.join(directory,i)

        ope = dt.datetime.now().timestamp() - os.stat(file).st_birthtime
        if ope >= 604800 and os.path.splitext(file)[1] == '.temp': os.remove(file)

#-Using
tempRoutine(myDir)