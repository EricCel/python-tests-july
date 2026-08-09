#Add 45 days and 12 hours to the current date and time, and print the result in a readable format.

#-Importing:
import datetime as dat

#-Operation:
today = dat.datetime.today() #Today
destiny = today + dat.timedelta(days=45,hours=12) #Next date

#-Printing in readable format:
formated = dat.datetime.strftime(destiny,'%B %dth, %Y')
print(formated)