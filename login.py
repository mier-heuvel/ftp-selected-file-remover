""" Script to sign into FTP server. """

from ftplib import FTP

host = input('Please enter host address: ')
user = input('Please enter username: ')
password = input('Please enter password: ')

def loginftp():
    ftp = FTP(host)
    ftp.login(user, password)
    print(ftp.getwelcome())

