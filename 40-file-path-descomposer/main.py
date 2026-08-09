#Use os.path.split() and os.path.splitext() to decompose a full path into: directory path, file base name, and file extension.

#-Importing:
import os

#-Descomposing:
def descompose(file):
    path = os.path.split(file)
    name = os.path.splitext(path[1])
    return path[0], name[0], name[1]

#-Displaying:
path,name,extension = descompose(__file__)
print(f'path: {path}\nname: {name}\nextension: {extension}')