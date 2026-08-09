#Write a script that searches for all files with a .txt extension in a folder and renames them by changing their extension to .log.

#-Importing:
import os

#-Getting Directory:
logsDir = os.path.join('39-file-type-search','logs')

#-Creating Function:
def transExtension(dir, pre, post):
    for i in os.listdir(dir):
        file = os.path.splitext(i)
        if file[1] == pre:
            os.rename(os.path.join(dir,i),os.path.join(dir,f'{file[0]}{post}'))

#-Using Function:
transExtension(logsDir,'.txt','.log')