#-Description:Calculate how many days are left until your next birthday using the datetime module.

#-Importing:
from datetime import date

#-Creating the function:
def daysUntil(m,d, y = None):
    #Today:
    today = date.today()

    match y:

        #If year is given:
        case int(y):
            destiny = date(y, m, d) #destiny
            if destiny <= today : today = date(y - 1,today.month, today.day) #Condition

        #If no year is given:
        case _:
            destiny = date(today.year, m, d) #destiny
            if destiny <= today : today = date(today.year - 1,today.month, today.day) #Condition

    #Return days until:
    return (destiny - today).days 

print(daysUntil(10,30,2028))