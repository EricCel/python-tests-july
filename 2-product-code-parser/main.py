#Create a parser for parts of a product code formatted as “CAT-YEAR-ID-LOC” using string slicing.
#System:
prod_code = "CAT-2024-ABC12345-TEXAS"
data = ['1:Manufacturer', '2:Year', '3:Identification', '4:Location']
select = prod_code.split('-')

#Program
while True:
    try:
        part = select[int(input("What part of the code do you want?('1:Manufacturer', '2:Year', '3:Identification', '4:Location')")) - 1]
    except:
        print("Invalid range")
    else:
        result = f'{data[select.index(part)]}: {part}'
        print(result)
        break