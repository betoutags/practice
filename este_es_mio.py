import os
if os.name == "nt":
   command = "dir"
else:
   command = "ls -l"
os.system(command)

# this is a nice add


