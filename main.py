from urllib import request



# Define the remote file to retrieve
remote_url = 'https://upload.wikimedia.org/wikipedia/commons/b/b5/International_Morse_Code.svg'

# Define the local filename to save data
local_file = 'File_p1.svg'




# Download remote and save locally
request.urlretrieve(remote_url, local_file)