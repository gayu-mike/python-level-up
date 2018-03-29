from ctypes import *


def create_file(win):
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
    GENERIC_READ = 0x80000000
    GENERIC_WRITE = 0x40000000
    OPEN_EXISTING = 3

    pipe = win.CreateFileW(
        '\\\\.\\pipe\\wg0',
        GENERIC_READ | GENERIC_WRITE,
        0,
        None,
        OPEN_EXISTING,
        0,
        None
    )
    print('create read pipe', pipe)
    if pipe == -1:
        print(win.GetLastError())
    return pipe


def set_pipe_mode(win, pipe):
    """
    """
    PIPE_READMODE_MESSAGE = 0x00000002

    mode = c_ulong(PIPE_READMODE_MESSAGE)
    success = win.SetNamedPipeHandleState(
        pipe,
        byref(mode),
        None,
        None
    )
    return success


def read_file(win, pipe):
    """
    BOOL WINAPI ReadFile(
      _In_        HANDLE       hFile,
      _Out_       LPVOID       lpBuffer,
      _In_        DWORD        nNumberOfBytesToRead,
      _Out_opt_   LPDWORD      lpNumberOfBytesRead,
      _Inout_opt_ LPOVERLAPPED lpOverlapped
    );
    """
    buf_size = 255
    buf = create_string_buffer(buf_size)
    read = c_ulong(0)
    success = win.ReadFile(
        pipe,
        buf,
        buf_size,
        byref(read),
        None
    )
    print(buf.value)
    return success


def main():
    win = windll.kernel32
    pipe = create_file(win)
    if set_pipe_mode(win, pipe):
        read_file(win, pipe)


if __name__ == '__main__':
    main()
