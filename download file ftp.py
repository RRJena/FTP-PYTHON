from ftplib import FTP
import os # allows me to use os.chdir

port=21
ip="192.168.3.145"
password='1234'

os.chdir("D:/") #changes the active dir - this is where downloaded files will be saved to
ftp = FTP("192.168.3.145")
ftp.login('ADMIN',password)
print ("File List:")
files = ftp.dir()

directory ="/" #dir i want to download files from, can be changed or left for user input
filematch = '*.*' # a match for any file in this case, can be changed or left for user to input

ftp.cwd(directory)

for filename in ftp.nlst(filematch): # Loop - looking for matching files
    fhandle = open(filename, 'wb')
    print('Getting ' + filename) #for confort sake, shows the file that's being retrieved
    ftp.retrbinary('RETR ' + filename, fhandle.write)
    fhandle.close()
