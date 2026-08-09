#Read a plain text file line by line, remove line breaks, and save only the lines containing a specific keyword into a new file.
#-File's Name:
fn = './26-file-keyword-search/stadistics.txt'
#-Appareances file:
af = './26-file-keyword-search/appareances.txt'
#-Opening appareances file:
with open(fn, "r") as f1, open(af, "w") as f2:
    #Getting keyword appareances:
    keyword = f1.readlines()
    appareances = [i for i in keyword if "great" in i]
    print(appareances)
    #Writing appareances:
    for i in appareances:f2.write(i)