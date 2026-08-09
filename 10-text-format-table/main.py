#Write a script that uses escape characters (\n, \t, \") to print a formatted text table without using external libraries.
Name = 'Name:, Luis, Joseph, Rober'
Age = 'Age:, 1, 2, 3'
Couutry = 'Country:, Peru, England, Elsewhere'

def toTable(*Data):
    newData = [i.split("," or ".") for i in Data]
    for i in newData:
        for j in i:
            i[i.index(j)] = j.ljust(15," ")
    joining = [[j[i] for j in newData] for i in range(0,len(newData[0]))]
    separating = [f'{"\t".join(joining[i])}\n' for i in range(len(joining))]
    table = "".join([separating[i] for i in range(len(separating))])
    return table
print(toTable(Name,Age,Couutry))