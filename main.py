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

fileType = input("Enter the filetype: ") #jpg

loopStart = int(input("Start of the loop: ")) #1
loopEnd = int(input("End of the loop: "))+1 #130




for i in range (loopStart, loopEnd):
    print(i)

    # Define the path for the remote files to retrieve
    remote_url = 'https://upload.wikimedia.org/wikipedia/commons/a/a3/Paleospace-'+str(i)+'.'+fileType 
    print(remote_url)

    # Define the local filenames to save data    
    local_file = dirName+'/File'+str(i)+'.'+fileType
    print(local_file)

    # Download remote and save locally
    request.urlretrieve(remote_url, local_file)



