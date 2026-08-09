#Write a folder organizer that automatically moves files into subfolders based on their extension (images, documents, audio).

#-Importing:
import os

#-Getting directory:
myDir = os.path.dirname(__file__)

#-Creating function:
def orgExt(directory):
    #Setting up:
    files = os.listdir(directory)

    #Organizing
    for i in files:
        file = os.path.splitext(i)
        os.renames(os.path.join(directory,i), os.path.join(directory,file[1][1::],i))

#-Using:
orgExt(myDir)
