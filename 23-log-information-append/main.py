#Create a log recording system in a .txt file by appending lines with the date and an event description.
import datetime as da, random as ra

generatedN = ra.randint(0,255)
with open('./23-log-information-append/log.txt','+a') as f:
    f.write(f'{da.datetime.now()}, {generatedN}\n')