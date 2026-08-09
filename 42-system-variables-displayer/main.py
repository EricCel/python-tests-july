#Read your operating system's environment variables storing the user name and system path

import os #-Importing

sys_user = os.getenv('USERNAME')#-User
sys_path = os.getenv('PATH')#-Path
print(f"{sys_user}'s system path is {sys_path}")#-Displaying