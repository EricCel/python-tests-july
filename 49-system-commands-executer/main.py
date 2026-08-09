#Read commands from the console and execute a simple operating system command using os.popen(), capturing its output in a variable.

#-Importing:
import os

#-Executing command:
inpute = os.popen('dir')

#-Capturing input:
outpute = inpute.read()

#-Returning input:
print(outpute)

#-Closing cmd:
inpute.close()