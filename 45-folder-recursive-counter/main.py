#Use os.walk() to recursively scan a folder and count how many total files exist across all its subfolders.

#-Importing:
import os

#-My CURRENT folder:
my_folder = os.path.dirname(os.path.dirname(__file__))

#-Total Files for all subfolders:
def total_recursive(folder):
    total = 0
    for folder,sub,files in os.walk(folder):
            total += len(files)
    return total

#-Recursive Scan:
def scan_recursive(folder):
    for folder,sub,files in os.walk(folder):
        print(f'====={os.path.split(folder)[1]}=====\nsubfolders:{len(sub)}, files:{len(files)}\n')

#-Count files for every subfolder:
def get_recursive(folder):
    directory = {}

    for folder,sub,files in os.walk(folder):
        directory[os.path.split(folder)[1]] = (len(sub),len(files))

    return directory

#-Folder with most files:
def most_recursive(recursive):
    most = sorted(recursive,key=lambda x: recursive[x][1])
    return most[-1], recursive[most[-1]][1]





#-Using functions:
total = total_recursive(my_folder)
print(total)

scan_recursive(my_folder)

gotten = get_recursive(my_folder)
print(gotten)

name, quantity = most_recursive(gotten)
print(name,quantity)
