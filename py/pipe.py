import os
import threading
import time


def rpipe(f):
    print('Starting rpipe')
    print('Read from pipe {}'.format(f.read()))


def wpipe(f):
    print('Starting wpipe')
    msg = 'echo'
    print('Write to pipe')
    f.write(msg)


def main():
    rfd, wfd = os.pipe()
    rfile = os.fdopen(rfd, 'r')
    wfile = os.fdopen(wfd, 'w')
    rt = threading.Thread(target=rpipe, args=(rfile,))
    # wt = threading.Thread(target=wpipe, args=(wfile,))
    rt.start()
    time.sleep(30)
    # wt.start()
    wfile.write('echo')


if __name__ == '__main__':
    main()
