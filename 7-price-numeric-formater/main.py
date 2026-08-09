#Create a price formatter that receives an integer or float and displays it as currency (e.g., $1,250.50).
price = 1250.50

def formatPRICE(price='123456.78', currencySymbol='$', mode=0):
    try:
        price = float(price)
        if mode in [0,1]:
            match mode:
                case 0: thousands, decimals = ",", "."
                case 1: thousands, decimals = ".", ","
        else:
            raise ZeroDivisionError
        
    except ZeroDivisionError:
        return "Must be between 0 and 1"
    except ValueError:
        return "Invalid data, must be a number"
    
    else:
        priceOG = str(price).split(".")
        intPart = priceOG[0][::-1]
        decimalPart = priceOG[1]
        separated = []
        for i in range(0,len(intPart),3):
            separated.append(intPart[i:i + 3])
        return f'{currencySymbol}{thousands.join(separated)[::-1]}{decimals}{decimalPart}'

print(formatPRICE(price=price))