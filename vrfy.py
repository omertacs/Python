#!/usr/bin/python

###
#  a simple script that iterates a file containing user names to check if the user exists on a SMTP server (using "VRFY")
####

import socket
import sys

with open('users.txt', 'r') as f:
        users = f.readlines() # creates an array of users ["user1", "user2", ...etc"]
        
        
'''
TODO: Make server and file user input

if len(sys.argv) != 2:
print("Usage: vrfy.py <usernames>"
sys.exit(0)

'''


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket
connect=s.connect(('10.11.1.227',25)) #connect to the server
banner=s.recv(1024)
print(banner)
for i in users:
        if i != users[-1]:
                user = i.strip()
                s.send("VRFY " + user + '\r\n') # vrfy a user
                result=s.recv(1024)
                print(result)
        else:
                s.send("QUIT") # closes the connection to the SMTP server
s.close()

