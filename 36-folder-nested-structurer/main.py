#Build a program that creates a nested folder structure (e.g., Project/Data/Processed) only if it does not already exist.

#-Importing:
import os

#-Directory:
directory = os.path.split(os.path.abspath(__file__))[0]

#-Nested folders:
nestedFolders = os.path.join(directory,'Project','Data','Processed')

#-Making dirs:
os.makedirs(nestedFolders,exist_ok=False)