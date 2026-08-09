#Traverse a directory and print each file's name, size in Kilobytes (KB), and last modification date:

import os
from datetime import datetime as dat

thisDir = os.path.split(os.path.abspath(__file__))[0]

for i in os.listdir(thisDir):
    file = os.stat(os.path.join(thisDir,i))
    print(f'{i}: size:{file.st_size / 1024:.2f}kb, modificated: {dat.fromtimestamp(file.st_mtime)}')