#Query full file metadata using os.stat() and print the creation date and size in bytes on the screen.

#-Importing
import os, string
from datetime import datetime as dat

#-My file:
file = __file__

#-Query:
meta = os.stat(file)

#-Create data to display:
default = string.Template(f'The file was created at $d\nPosseses a size of $s bytes')

udate = dat.strftime(dat.fromtimestamp(meta.st_birthtime),'%B %dth, %Y')
usize = meta.st_size


#-Displaying metadata:
display = default.substitute(d=udate, s=usize)
print(display)