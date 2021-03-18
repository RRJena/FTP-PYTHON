import sys
import ftplib
import os
import time

server = "192.168.3.145"
user = "ADMIN"
password = "1234"
source = "/"
destination = "D:/"
interval = 0.05

ftp = ftplib.FTP(server)
ftp.login(user, password)


def downloadFiles(path, destination):
    try:
        ftp.cwd(path)       
        os.chdir(destination)
        mkdir_p(destination[0:len(destination)-1] + path)
        print ("Created: " + destination[0:len(destination)-1] + path)
    except OSError:     
        pass
    except ftplib.error_perm:       
        print ("Error: could not change to " + path)
        sys.exit("Ending Application")
    
    filelist=ftp.nlst()

    for file in filelist:
        time.sleep(interval)
        try:            
            ftp.cwd(path + file + "/")          
            downloadFiles(path + file + "/", destination)
        except ftplib.error_perm:
            os.chdir(destination[0:len(destination)-1] + path)
            
            try:
                ftp.retrbinary("RETR " + file, open(os.path.join(destination + path, file),"wb").write)
                print ("Downloaded: " + file)
            except:
                print ("Error: File could not be downloaded " + file)
    return
    
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        print("ERROR)]")

downloadFiles(source, destination)
