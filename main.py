import os
from urllib import request

# Create directory
dirName = input("Enter a folder name: ")
try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Folder created ") 
except FileExistsError:
    print("Directory " , dirName ,  " Folder already exists")

fileType = input("Enter the filetype: ")

loopStart = input("Start of the loop:")
loopEnd = input("End of the loop:")

# Define the path for the remote files to retrieve
remote_url = 'https://upload.wikimedia.org/wikipedia/commons/b/b5/International_Morse_Code.svg'

# Define the local filenames to save data
local_file = dirName+'/File_p1'+'.'+fileType




# Download remote and save locally
request.urlretrieve(remote_url, local_file)