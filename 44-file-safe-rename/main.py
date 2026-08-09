#Implement a safe file rename using os.replace() to ensure the operation is atomic.

#-Importing
import random as ra, os

#-Files:
myDir = os.path.dirname(__file__)
filesDir = os.listdir(myDir)

#-Renaming:
os.replace(os.path.join(myDir,filesDir[0]),os.path.join(myDir,str(ra.randint(0,256))))