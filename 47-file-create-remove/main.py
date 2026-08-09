#Generate a test .txt file, wait 3 seconds using time.sleep(), delete it with os.remove(), and confirm its deletion.

#-Importing:
import os, time

#-Directory and file:
my_Dir = os.path.dirname(__file__)
new_file = os.path.join(my_Dir,'test.txt')

#-Creating the file:
with open(new_file, 'w') as f: f.write('File')

#-Waiting:
time.sleep(3)

#-Deleting:
os.remove(new_file)

#-Confirming:
if not os.path.exists(new_file): print('File deleted succesively!')