#Ask the user for a text date in the format "DD/MM/YYYY" and convert it to a datetime object formatted as "YYYY-MM-DD".

#-Importing:
import datetime

#-Requesting:
userDate = input("Please, insert a date in the format 'DD/MM/YYYY': ")

#-Returning date object
systemDate = datetime.datetime.strptime(userDate,"%Y/%m/%d"); print(systemDate)