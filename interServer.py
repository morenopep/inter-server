#!/usr/bin/python

import socket

print "Interagindo com FTP SERVER!"

ip = raw_input("Digite o IP: ")
porta = 21
meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect((ip,porta))
banner = meusocket.recv(1024)
print banner

print "Enviando usuario"
meusocket.send("USER teste\r\n")
banner = meusocket.recv(1024)
print banner

print "Enviando senha"
meusocket.send("PASS teste\r\n")
banner = meusocket.recv(1024)
print banner