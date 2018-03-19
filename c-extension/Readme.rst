.. _ctypes:

ctypes
------

**ctypes提供C语言的类型, 以及调用DLL或者share library里的函数的接口.**

tutorial
~~~~~~~~

.. note::

    doctest

.. note::

    sizeof(long) == sizeof(int)

.........
载入动态库
.........

Linux下的载入方法, 注意要输入文件拓展名:

.. code-block:: python3

    >>> from ctypes import *
    >>> cdll.LoadLibrary("libc.so.6")  
    <CDLL 'libc.so.6', handle ... at ...>
    >>> libc = CDLL("libc.so.6")       
    >>> libc                           
    <CDLL 'libc.so.6', handle ... at ...>

与上述相当的C标准库载入, Windows可以不输入拓展名:

.. code-block:: python3

    >>> print(cdll.msvcrt)      
    <CDLL 'msvcrt', handle ... at ...>
    >>> libc = cdll.msvcrt 
    # windows
    >>> print(windll.kernel32)  
    <WinDLL 'kernel32', handle ... at ...>
    # 载入自己写的动态库
    >>> mylib = WinDLL('mylib.dll')

............
获取动态库函数
............

一般来说就是用``.``访问库函数:

.. code-block:: python3

    >>> libc.printf
    <_FuncPtr object at 0x...>
    >>> print(windll.kernel32.GetModuleHandleA)
    <_FuncPtr object at 0x...>

windows毕竟比较奇葩, 首先你要注意**Unicode函数的尾缀是W, ANSI函数的尾缀是A**,
其次, 你可能要用``getattr(cdll.msvcrt, "??2@YAPAXI@Z")``来访问奇葩命名的函数,
最后, 有一些函数不是根据函数名来访问, 而是使用序列来访问的:

.. code-block:: python3

    >>> cdll.kernel32[1]  
    <_FuncPtr object at 0x...>

.......
数据类型
.......

Python本身的数据类型中, 有对应C的数据类型:

- None >>> void\*
- bytes >>> char\*
- str >>> wchar_t\*
- int >>> int

其余的数据类型请参考:
`C compatible data types _<https://docs.python.org/3/library/ctypes.html?highlight=ctypes#fundamental-data-types>`

获取它们的值:

.. code-block:: python3

    >>> i = c_int()
    >>> print(i)
    c_long(0)
    >>> i = 42
    >>> print(i.value)
    42

**因为Python的实现中, bytes/str是不可变的, 所以如果你使用``c_char_p``/``c_wchar_p``/``c_void_p``
并为它们赋值, 实际上它们会改变地址.(在C中指针改变指向的地址自己的地址是不改变的)**

.. code-block:: python3

    >>> c_s = c_wchar_p("hello")
    >>> print(c_s)
    c_wchar_p(4337521456)
    >>> c_s.value
    'hello'
    >>> c_s.value = "world"
    >>> c_s
    c_wchar_p(4337521480)

因此, 如果你需要不可变的指针, 需要使用``create_string_buffer()``/``create_unicode_buffer()``.

.. todo:: example

....
调用
....

调用函数使用``()``语法:

.. code-block:: python3

    >>> print(libc.time(None))  
    1150640792
    >>> print(hex(windll.kernel32.GetModuleHandleA(None)))  
    0x1d000000

.. note::

    cdll使用cdel calling convention, windll使用stdcall calling convention,
    如果你把两者搞反了, 会抛出ValueError.

.. code-block:: python3

    >>> cdll.kernel32.GetModuleHandleA(None)  
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Procedure probably called with not enough arguments (4 bytes missing)
    >>>

    >>> windll.msvcrt.printf(b"spam")  
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Procedure probably called with too many arguments (4 bytes in excess)
    >>>

**faulthandler**

看一个printf的例子, 它解释了ctypes中简单的传参:

.. code-block:: python3

    >>> printf = libc.printf
    >>> printf(b"Hello, %s\n", b"World!")
    Hello, World!
    14
    >>> printf(b"Hello, %S\n", "World!")
    Hello, World!
    14
    >>> printf(b"%d bottles of beer\n", 42)
    42 bottles of beer
    19
    >>> printf(b"%f bottles of beer\n", 42.5)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ArgumentError: argument 2: exceptions.TypeError: Don't know how to convert parameter 2
    >>> printf(b"%f bottles of beer\n", c_double(42.5))
    42.5 bottles of beer
    2

C和Python不同的一点是, 它是声明式强类型的, 比如:

.. code-block:: c

    int add(int, int);

在ctypes中也可以指定参数类型, 起到类似声明的作用:

.. code-block:: python3

    >>> printf.argtypes = [c_char_p, c_char_p, c_int, c_double]
    >>> printf(b"String '%s', Int %d, Double %f\n", b"Hi", 10, 2.2)
    String 'Hi', Int 10, Double 2.200000
    37
    >>> printf(b"%d %d %d", 1, 2, 3)    # 传入错误类型参数
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ArgumentError: argument 2: exceptions.TypeError: wrong type
    >>> printf(b"%s %d %f\n", b"X", 2, 3)   # 类型转换
    X 2 3.000000
    13

以及指定返回类型(不指定的话默认是``int``):

.. code-block:: python3

    >>> strchr = libc.strchr
    >>> strchr(b"abcdef", ord("d"))  
    8059983
    >>> strchr.restype = c_char_p    # c_char_p is a pointer to a string
    >>> strchr(b"abcdef", ord("d"))
    b'def'
    >>> print(strchr(b"abcdef", ord("x")))

上面``ord(‘x')``是取Python字符对应的C字符, 如果使用``strchr.argtypes = [c_char_p, c_char]``
限定参数, 可以直接传参``b'x'``进去.

.. todo:: 再看看如何传自定义的参数: _as_parameter_ example

.. todo:: from_parameter example

.. todo:: Python函数作为返回值

.....
array
.....

.......
pointer
.......

C语言有pointer类型而Python没有, 下面就来看看ctypes中的pointer.

有时候我们需要reference一个数据的地址, 比如作为函数参数. ctypes提供了``byref()``:

.. code-block:: python3

    >>> i = c_int()
    >>> f = c_float()
    >>> s = create_string_buffer(b'\000' * 32)
    >>> print(i.value, f.value, repr(s.value))
    0 0.0 b''
    >>> libc.sscanf(b"1 3.14 Hello", b"%d %f %s",
    ...             byref(i), byref(f), s)
    3
    >>> print(i.value, f.value, repr(s.value))
    1 3.1400001049 b'Hello'

但有时候我们需要一个真正的pointer, 这时候就要用上``pointer()``:

.. code-block:: python3

    >>> i = c_int(22)       # int i = 22;
    >>> pi = pointer(i)     # int *pi = &i;
    >>> pi.content          # *pi;
    >>> ip = POINTER(c_int) # int *ip;
    >>> ip(i)               # ip = &i;
    >>> POINTER(c_int(22))  # 同上
    >>> POINTER(c_int)()    # NULL pointer

.......
类型转换
.......

ctypes做严格的类型检查, 就是说: 如果参数/返回值指定了一个类型, 那么值必须是这个类型.
(这里我们可以单纯用C语言的思维来理解.)

另外有个也比较符合C语言的特例, 就是指针和数组作为参数传入时可以视为等同:

.. code-block:: python3

    class Bar(Structure):
        _fields_ = [('count', c_int), ('values', POINTER(c_int))]

    bar = Bar()
    bar.count = 3
    bar.values = (c_int * 3)(1, 2, 3)
    for i in range(bar.count):
        print(bar.values[i])

    # null pointer
    bar.values = None

.. todo::
    pointer c_int and c_int and byref()

因此, 有时我们需要类型转换. Python内置了一些类型转换的函数:

.. code-block:: python3

    >>> i = c_int(1)
    >>> float(i.value)
    1.0
    >>> str(i.value)
    '1'

同时, 也提供了和C语言一样的 ``cast``, 转换指针对象里面的数据类型:

.. code-block:: python3

    >>> a = (c_byte * 4)()
    >>> a
    <__main__.c_byte_Array_5 object at 0x0000000002875648>
    >>> b = cast(a, POINTER(c_int))     # cast() returns a new object
    >>> b
    <__main__.LP_c_long object at 0x00000000028756C8>

.........
structure
.........

ctypes里提供了``Structure``类和``Union``类, 结构体的成员使用``_fields_``属
性来定义. fields必须是一个``list``, 里面的每个元素都是一个``2-tuple``,
tuple中的2个元素分别是: member name / member type

.. code-block:: python3

    class POINT(Structure):
         _fields_ = [("x", c_int),
                     ("y", c_int)]

    >>> point = POINT(10, 20)
    >>> print(point.x, point.y)
    10 20
    >>> point = POINT(y=5)
    >>> print(point.x, point.y)
    0 5
    >>> POINT(1, 2, 3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: too many initializers

当然, 和C一样, 也可以把结构体作为结构体成员:

    class RECT(Structure):
        _fields_ = [
            ('upperleft', POINT),
            ('lowerright', POINT)
        ]

    >>> rc = RECT(point)
    >>> print(rc.upperleft.x, rc.upperleft.y)
    0 5
    >>> print(rc.lowerright.x, rc.lowerright.y)
    0 0
    >>> r = RECT(POINT(1, 2), POINT(3, 4))
    >>> r = RECT((1, 2), (3, 4))

........
callback
........

**callback就是函数指针()**

创建一个callback, 首先用``CFUNCTYPE``声明, 要传入:

0. return type
1. 余下的是callback接收的参数

在定义了Python callback函数之后, 初始化这个函数, 最后把callback放到C函数要用到这个
callback的参数位置即可.

.. code-block:: python3

    CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))      # unix
    CMPFUNC = WINFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))    # windows

    def cmp(a, b):
        return a[0] - b[0]

    callback = CMPFUNC(cmp)

    # ...省略

    qsort(ia, len(ia), sizeof(c_int), callback)

reference
~~~~~~~~~