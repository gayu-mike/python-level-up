from ctypes import *


def create_named_pipe(win):
    """ Create a named pipe.

    This is a wrapping function of Windows CreateNamedPipe.

    HANDLE WINAPI CreateNamedPipe(
      _In_     LPCTSTR               lpName,
      _In_     DWORD                 dwOpenMode,
      _In_     DWORD                 dwPipeMode,
      _In_     DWORD                 nMaxInstances,
      _In_     DWORD                 nOutBufferSize,
      _In_     DWORD                 nInBufferSize,
      _In_     DWORD                 nDefaultTimeOut,
      _In_opt_ LPSECURITY_ATTRIBUTES lpSecurityAttributes
    );
    """
    PIPE_ACCESS_DUPLEX = 0x00000003
    # PIPE_ACCESS_OUTBOUND = 0x00000002
    # PIPE_TYPE_BYTE = 0x00000000
    PIPE_READMODE_MESSAGE = 0x00000002
    PIPE_TYPE_MESSAGE = 0x00000004
    PIPE_WAIT = 0x00000000
    PIPE_UNLIMITED_INSTANCES = 255
    BUFFER_SIZE = 2048
    NMPWAIT_USE_DEFAULT_WAIT = 0

    # name = c_wchar_p('\\\\.\\pipe\\wireguard-ipc-wg0')
    pipe = win.CreateNamedPipeW(
        '\\\\.\\pipe\\wg0',
        PIPE_ACCESS_DUPLEX,
        PIPE_TYPE_MESSAGE | PIPE_READMODE_MESSAGE | PIPE_WAIT,
        PIPE_UNLIMITED_INSTANCES,
        BUFFER_SIZE,
        BUFFER_SIZE,
        NMPWAIT_USE_DEFAULT_WAIT,
        None,
    )
    print(pipe)
    if pipe == -1:
        print('Create pipe failed with code: {}'.format(win.GetLastError()))
    return pipe


def write(win, pipe):
    """ Write to a named pipe.

    This is a wrapping function of Windows WriteFile.

    BOOL WINAPI WriteFile(
      _In_        HANDLE       hFile,
      _In_        LPCVOID      lpBuffer,
      _In_        DWORD        nNumberOfBytesToWrite,
      _Out_opt_   LPDWORD      lpNumberOfBytesWritten,
      _Inout_opt_ LPOVERLAPPED lpOverlapped
    );
    """
    msg = b'hello from server.'
    written = c_ulong(0)
    success = win.WriteFile(
        pipe,
        c_char_p(msg),
        len(msg),
        byref(written),
        None
    )
    if not success:
        print(win.GetLastError())


def connect_pipe(win, pipe):
    """ See if the named pipe is connected.

    This is a wrapping function of Windows ConnectNamedPipe.
    This function will block its thread,
    if the pipe is connected by a client, returns True.
    """
    success = win.ConnectNamedPipe(pipe, None)
    return success


def main():
    win = windll.kernel32
    pipe = create_named_pipe(win)
    if connect_pipe(win, pipe):
        # p = threading.Thread(target=handle_client)
        write(win, pipe)


if __name__ == '__main__':
    main()
