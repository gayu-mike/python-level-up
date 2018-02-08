import socket
import sys


HOST = ''
PORT = 8888


s = socket.socket()

try:
	s.bind((HOST,PORT))
except socket.error, msg:
	print 'Bind failed %s' % msg
	sys.exit()

print 'socket bind complete'

print 'waiting for message...'
while True:
    s.listen(1)
    conn, addr = s.accept()
    conn.sendall(b'1')

conn.close()
s.close()
