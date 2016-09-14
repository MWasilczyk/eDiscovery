# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:53:59 2016

Create a file named "ServerList.list" which includes server on one line:
    SERVER.FQDN:PORT

Displays the number of servers and the names of each during processing.

Creates a file for each server/protocol combination, and writes the results 
of the OpenSSL probe.

@author: mikew
"""
import subprocess

InputFile = 'ServerList.list'
InstallationDirectory = 'C:\\OpenSSL-Win32\\bin\\openssl'
ProtocolList = ['-ssl2','-ssl3','-tls1','-tls1_1','-tls1_2']

with open(InputFile, 'r') as ServerList:
    ServerNames = ServerList.readlines()
    print('Number of Servers: \r\n  ' + str(len(ServerNames)))
    print('Server Names: ')
    for i in ServerNames:
        print('  ' + i.split('.')[0])
        for x in ProtocolList:
            with open(i.split('.')[0] + x + '.txt', 'w') as CurrentServer:      
                pro = subprocess.Popen([InstallationDirectory, 's_client', x, '-connect', i.strip()],stdout=CurrentServer, stderr=subprocess.PIPE, stdin=subprocess.PIPE)   