import socket
import sys


host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print(e)
    sys.exit(1)

try:
    port = int(textport)
except ValueError:
    try:
        port = socket.getservname(textport, 'tcp')
    except socket.error as e:
        print(e)
        sys.exit(1)

try:
    s.connect((host, port))
except (socket.gaierror, socket.error) as e:
    print(e)
    sys.exit(1)

try:
    s.sendall('GET {} HTTP/1.1\r\nhost: {}\r\n\r\n'.format(filename, host).encode())
except OSError as e:
    print(e)
    sys.exit(1)


while True:
    try:
        buf = s.recv(2048)
    except socket.error as e:
        print(e)
        sys.exit(1)
    if len(buf) == 0:
        break
    print(buf)
