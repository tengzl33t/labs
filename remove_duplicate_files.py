from tkinter.filedialog import askdirectory
from tkinter import Tk
import os, hashlib
import sys
from pathlib import Path

hashes = dict()
Tk().withdraw()
path=askdirectory(title= "Selecte the folder!")
print ("Looking for duplicate files in: " + path)
# files_list = os.listdir(path) # List files and Directory
#List only files
files_list = (file for file in os.listdir(path) 
         if os.path.isfile(os.path.join(path, file)))

for file in files_list:
    # print(file) #Print Files Names
    file_name = Path(os.path.join(path, file))
    # print(file_name)#Print Files path
    if file_name.is_file():
        file_hash = hashlib.md5(open(file_name, 'rb').read()).hexdigest()
        # print(file_hash) #Print the hash values
        if file_hash not in hashes:
            hashes[file_hash] = file_name
        else:
            print("\n" + str(file_name) + " " + "is a duplicate file!")
            if input("\nEnter (y)es to confirm deletion or anything else to abort: ").lower() not in ("y", "yes"):
                sys.exit("Operation cancelled by user. Exiting...")
            print("\nDeleting...")
            os.remove(file_name)
            print(str(file_name) + " " + "File has been removed!")
    else:
        print("Operation failed!")