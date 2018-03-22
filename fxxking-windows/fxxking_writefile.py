from ctypes import *


generic_read = 0x80000000
generic_write = 0x40000000
file_lock = 0
create_new = 1
open_always = 4
normal = 0x80


def create_file(path, access=generic_read, mode=file_lock, secure=None,
                disposition=open_always, flags=normal, template=None):
    """
    HANDLE WINAPI CreateFile(
      _In_     LPCTSTR               lpFileName,
      _In_     DWORD                 dwDesiredAccess,
      _In_     DWORD                 dwShareMode,
      _In_opt_ LPSECURITY_ATTRIBUTES lpSecurityAttributes,
      _In_     DWORD                 dwCreationDisposition,
      _In_     DWORD                 dwFlagsAndAttributes,
      _In_opt_ HANDLE                hTemplateFile
    );
"""
    fd = windll.kernel32.CreateFileW(path, access, mode, secure,
                                     disposition, flags, template)
    return fd


def write_file(fd, msg):
    msg = msg.encode()
    written = c_ulong(0)
    success = windll.kernel32.WriteFile(fd, c_char_p(msg), len(msg),
                                        byref(written), None)
    return success


def close_file(fd):
    return windll.kernel32.CloseHandle(fd)


def main():
    # fd = create_file('fxxking_test.txt', access=generic_write)
    fd = create_file('fxxking_test.txt')
    print(fd)
    success = write_file(fd, 'fuck windows')
    print(success)
    # if write_file(fd, 'fuck windows'):
    #     print('windows sucks')
    return close_file(fd)


if __name__ == '__main__':
    main()
