#Build a verifier that determines whether a given path is a file, a directory, or a symbolic link.

#-Importing:
import os

#-File:
file = r'.\46-system-structures-verifier\dirtest'

#-Verifier:
if os.path.isfile(file):
    print('Is a file')
elif os.path.isdir(file):
    print('Is a directory')
elif os.path.islink(file):
    print('Is a symlink')
else:
    print('Undetermined')