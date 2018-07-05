"""FTP script to remove select files from a defined date off a server"""

from ftplib import FTP

mdtm = "MDTM "

host = input('Please enter host address: ')
user = input('Please enter username: ')
password = input('Please enter password: ')

ftp = FTP(host)
ftp.login(user, password)


welcome = ftp.getwelcome()
print(welcome)
direct = ftp.nlst('public_html')

file_list = []
while len(direct) > 0:
    for item in direct:
        if item.endswith(".php"):
            file_list.append(item)
        elif "." not in item:
            direct.append(item)

#file_list2 = []
for i in file_list:
    date = ftp.sendcmd(mdtm + i)
    if date.startswith("213 2015"):
        #file_list2.append(i)
        print(i)

#print(direct)
    


ftp.quit()
