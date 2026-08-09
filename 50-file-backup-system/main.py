#Design a backup script that copies the contents of one folder to another, ensuring that newer files are not overwritten.

#-Importing:
import os

#-My directory:
myDir = os.path.dirname(__file__)
dir1 = os.path.join(myDir,'directory1')
dir2 = os.path.join(myDir,'directory2')

#-Function:
def backup(origin,destiny):
    for i in os.listdir(origin):
        copy = os.path.join(destiny,i)

        with open(os.path.join(origin, i),'r') as f1:
            if os.path.exists(copy):
                pass 

            else:
                with open(os.path.join(destiny,i),'w') as f2:
                    f2.write(f1.read())
backup(dir1,dir2)