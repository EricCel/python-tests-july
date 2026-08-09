#Using the os module, get the absolute path of the directory where your script is located and display a list of all its files.

#-Importing:
import os

#-Absolute path:
absPath = os.path.abspath(__file__)

#-Directory files:
files = os.listdir(os.path.dirname(absPath))

#-Display all the files:
print(files)