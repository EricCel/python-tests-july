#Design a unit converter with an interactive menu (Celsius to Fahrenheit, Kilometers to Miles).
def units(data,mode,conversion):
    try:
        match mode:
            case 0:   
                match conversion:
                    case 0:result = f'{(data * 9/5) + 32:.2f}°F'
                    case 1:result = f'{(data - 32) * 5/9:.2f}°C'  
            case 1:   
                match conversion:
                    case 0:result = f'{data * 1609:.2f}Km'
                    case 1:result = f'{data / 1609:.2f}Miles'
        return result
    
    except:
        return "Invalid range or input"         

data = 32
print(units(data,1,1))