from ctypes import *


libc = CDLL('libc.dylib')
printf = libc.printf
sscanf = libc.sscanf

s = create_string_buffer(b"hello", 10)
printf(b"%s", s.value)
print()
print(repr(s.value))


qsort = libc.qsort
IntArray = c_int * 5
ia = IntArray(5, 1, 7, 33, 99)


def cmp(a, b):
    print('{} {}'.format(a[0], b[0]))
    return a[0] - b[0]


CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
callback = CMPFUNC(cmp)
qsort(ia, len(ia), sizeof(c_int), callback)

for i in ia:
    print(i)
